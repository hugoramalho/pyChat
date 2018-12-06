import json
import socketserver
import threading

from pyChat.servidor.bd_server.Services.Handler import *


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    lst_client = []

    def handle(self):
        """
        OBS: SE EU TROCAR PARA socket, LEMBRAR QUE O ATRIBUTO .request É O SOCKET CLIENTE
        segundo a documentação: 'self.request is the TCP socket connected to the client'
        """
        # Abaixo é instanciada uma conexão com o banco de dados:
        self.con_status = True
        cur_thread = threading.current_thread()
        # print("{} se conectou!".format(self.client_address))

        while self.con_status:
            self.dado = self.__receive__()
            # Abaixo, é obtido o tipo do dado entrante:
            try:
                print(self.dado)
                requestName = self.dado['request']
            except:
                print('Requisição fora do padrão e/ou Cliente se desconectou')
                requestName = 'finish'

            if requestName == 'login':
                feedback = MyRequestHandler(self.dado)
                if isinstance(feedback, DTP.InternalExceptions) is not True:
                    # dic_cliente guarda a tupla (endereco, porta) e a id do usuário:
                    dictClient = {'client_address': self.client_address, 'client_id': feedback.data.idd, 'client': self.request}
                    # Em seguida, dic_cliente é adicionado à lista de clientes
                    self.__class__.lst_client.append(dictClient)
                    print('Client has just made a connection! ', self.__class__.lst_client)
                    self.__send__(feedback)
                else:
                    self.__send__(feedback)

            elif requestName == 'send_message':
                feedback = MyRequestHandler(self.dado)
                if isinstance(feedback, DTP.Request):
                    id_dest = feedback.data.recipId
                    client_dest = self.__class__.search_client(id_dest)
                    if client_dest is not None:
                        self.__sendTo__(client_dest, feedback)
                    self.__send__(feedback)

            elif requestName == 'finish':
                self.finish()

            elif requestName == 'addFriend':
                feedback = MyRequestHandler(self.dado)
                idFriend = feedback.data.idd
                client_dest = self.__class__.search_client(idFriend)
                if client_dest is not None:
                    self.__sendTo__(client_dest, feedback)
                self.__send__(feedback)

            else:
                feedback = MyRequestHandler(self.dado)
                self.__send__(feedback)

    def __sendTo__(self, socketRequest, obj: DTP.DataTransfer):
        try:
            obj = obj.toJson()
            dado_str = json.dumps(obj)
            dado_bytes = bytes(dado_str, "utf-8")
            socketRequest.sendall(dado_bytes)
        except Exception as Expt:
            print(Expt)

    def __send__(self, obj: DTP.DataTransfer):
        try:
            obj = obj.toJson()
            dado_str = json.dumps(obj)
            dado_bytes = bytes(dado_str, "utf-8")
            self.request.sendall(dado_bytes)
        except Exception as Expt:
            print(Expt)


    def __receive__(self):
        try:
            dado_byte = self.request.recv(11264).strip()
            dado_str = str(dado_byte, 'utf-8')
            dado_obj = json.loads(dado_str)
            return(dado_obj)
        except Exception as Expt:
            print(Expt)

    def finish(self):
        self.__class__.finish_client(client_address = self.client_address)
        self.con_status = False

    @classmethod
    def lst_clients(cls):
        return(cls.lst_client)

    @classmethod
    def search_client(cls, id_client):
        for elem_client in cls.lst_client:
            if elem_client['client_id'] == id_client:
                return elem_client['client']

    @classmethod
    def finish_client(cls, **kwargs):
        #client_id = kwargs['client_id']
        client_address = kwargs['client_address']
        for elem_client in cls.lst_client:
            if elem_client['client_address'] == client_address:
                del(elem_client)



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # logging.info({'module': 'server', 'msg': 'Listening'})
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)