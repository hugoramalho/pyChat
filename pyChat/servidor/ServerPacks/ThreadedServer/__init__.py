import json
import socketserver
import threading

from pyChat.Services.Handler import *


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

            print(self.dado)
            response = MyRequestHandler(self.dado)



            if isinstance(response, DTP.InternalExceptions):
                self.__send__(response)

            elif isinstance(response, Responses.ResponseLogin):
                # dic_cliente guarda a tupla (endereco, porta) e a id do usuário:
                dictClient = {'client_address': self.client_address, 'client_id': response.user.idd, 'client': self.request}
                # Em seguida, dic_cliente é adicionado à lista de clientes
                self.__class__.lst_client.append(dictClient)
                print('Client has just made a connection! ', self.__class__.lst_client)
                self.__send__(response)

            elif isinstance(response, Responses.ResponseSendMessage):
                recipId = response.message.recipId
                socketRecipUser = self.__class__.search_client(recipId)
                # SE O CLIENTE DESTINATÁRIO ESTIVER ONLINE:
                if socketRecipUser is not None:
                    print('ResponseSendMessage : client online')
                    # A MENSAGEM É IMEDIATAMENTE ENCAMINHADA À SUA SESSÃO:
                    self.__sendTo__(socketRecipUser, response)
                self.__send__(response)

            elif isinstance(response, Responses.ResponseAddFriend):
                recipId = response.friendship.recipUser.idd
                socketRecipUser = self.__class__.search_client(recipId)
                # SE O CLIENTE DESTINATÁRIO ESTIVER ONLINE:
                if socketRecipUser is not None:
                    print('ResponseAddFriend : client online')
                    # A MENSAGEM É IMEDIATAMENTE ENCAMINHADA À SUA SESSÃO:
                    self.__sendTo__(socketRecipUser, response)
                self.__send__(response)

            elif isinstance(response, Responses.ResponseFriendshipAcepted):
                senderId = response.friendship.senderUser.idd
                socketSenderUser = self.__class__.search_client(senderId)
                # SE O CLIENTE DESTINATÁRIO ESTIVER ONLINE:
                if socketSenderUser is not None:
                    print('ResponseFriendshipAcepted : client online')
                    # A MENSAGEM É IMEDIATAMENTE ENCAMINHADA À SUA SESSÃO:
                    self.__sendTo__(socketSenderUser, response)
            else:
                self.__send__(response)

    def __sendTo__(self, socketRequest, obj: DTP.DataTransfer or DTP.InternalExceptions):
        try:
            obj = obj.toJson()
            dado_str = json.dumps(obj)
            dado_bytes = bytes(dado_str, "utf-8")
            socketRequest.sendall(dado_bytes)
        except Exception as Expt:
            pass

    def __send__(self, obj: DTP.DataTransfer or DTP.InternalExceptions):
        try:
            print(obj)
            obj = obj.toJson()
            print('agora toJson() '+str(obj))
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