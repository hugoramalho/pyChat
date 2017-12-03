import socketserver
import json
import threading
from bd_server import server_requests as request



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
                req = self.dado['req']
            except:
                print('Requisição fora do padrão e/ou Cliente se desconectou')
                req = 'finish'
                pass


            if req == 'login':
                dic_feedback = request.login_handle(**self.dado)
                if dic_feedback['feedback'] == 0:
                    if dic_feedback['senha'] == self.dado['senha']:
                        # dic_cliente guarda a tupla (endereco, porta) e a id do usuário:
                        dic_client = {}
                        dic_client['client_address'] = self.client_address
                        dic_client['client_id'] = dic_feedback['id_user']
                        # Em seguida, dic_cliente é adicionado à lista de clientes
                        self.__class__.lst_client.append(dic_client)
                        print('Cliente se conectou! ', self.__class__.lst_client)
                        self.__send__(dic_feedback)
                    else:
                        dic_feedback['feedback'] = 1
                        dic_feedback['Erro'] = 'Senha incorreta'
                        self.__send__(dic_feedback)
                else:
                    self.__send__(dic_feedback)

            elif req == 'carrega_contatos':
                dic_feedback = request.carrega_contat_handle(**self.dado)
                self.__send__(dic_feedback)

            elif req == 'carrega_conversa':
                dic_feedback = request.carrega_conv_handle(**self.dado)
                self.__send__(dic_feedback)

            elif req == 'envio_msg':
                dic_feedback = request.envio_msg_handle(**self.dado)
                self.__send__(dic_feedback)
                #ENVIAR PARA O DEST

            elif req == 'finish':
                self.finish()

            elif req == 'insere_user':
                dic_feedback = request.novo_user_handle(**self.dado)
                self.__send__(dic_feedback)

            elif req == 'busca_contato':
                dic_feedback = request.busca_contato_handle(**self.dado)
                self.__send__(dic_feedback)

            elif req == 'conexao':
                self.__send__(self.dado)

    def __send__(self, obj):
        try:
            dado_str = json.dumps(obj)
            dado_bytes = bytes(dado_str, "utf-8")
            self.request.sendall(dado_bytes)
        except Exception as Expt:
            print(Expt)
            pass

    def __receive__(self):
        try:
            dado_byte = self.request.recv(11264).strip()
            dado_str = str(dado_byte, 'utf-8')
            dado_obj = json.loads(dado_str)
            return(dado_obj)
        except Exception as Expt:
            print(Expt)
            pass

    def finish(self):
        self.__class__.finish_client(client_address = self.client_address)
        self.con_status = False

    @classmethod
    def lst_clients(cls):
        return(cls.lst_client)

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




if __name__ == "__main__":
    server = ThreadedTCPServer(('127.0.0.1', 3333), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)

    try:
        server_thread.start()
        print('<< Servidor ON! >>')
    except KeyboardInterrupt:
        sys.exit(0)

