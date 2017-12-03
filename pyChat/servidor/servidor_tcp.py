import socketserver
import json
from bd_server import server_requests as request



class MyTCPHandler(socketserver.BaseRequestHandler):
    """
        O handle é chamado toda vez que uma conexão é aceita pelo servidor
        
    """

    def handle(self):
        """
        OBS: SE EU TROCAR PARA socket, LEMBRAR QUE O ATRIBUTO .request É O SOCKET CLIENTE
        segundo a documentação: 'self.request is the TCP socket connected to the client'
        """
        # Abaixo é instanciada uma conexão com o banco de dados:
        self.con_status = True
        
        while self.con_status:

            self.dado = self.__receive__()

            # Abaixo, é obtido o tipo do dado entrante:
            req = self.dado['req']
            print(req)

            if req == 'login':
                dic_feedback = request.login_handle(**self.dado)
                if dic_feedback['feedback'] == 0:
                    if dic_feedback['senha'] == self.dado['senha']:
                        # dic_cliente guarda a tupla (endereco, porta) e a id do usuário:
                        dic_client = {}
                        dic_client['client_address'] = self.client_address
                        dic_client['client_id'] = dic_feedback['id_user']
                        # Em seguida, dic_cliente é adicionado à lista de clientes

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
            return(-1)

    def __receive__(self):
        try:
            print("{} se conectou!".format(self.client_address))
            dado_byte = self.request.recv(11264).strip()
            dado_str = str(dado_byte, 'utf-8')
            dado_obj = json.loads(dado_str)
            return(dado_obj)
        except Exception as Expt:
            print(Expt)
            return(-1)


    
    #~ def finish(self):
        #~ print("{} se desconectou!".format(self.client_address))
        #~ #A atribuição abaixo interrompe o loop:
        #~ self.con_status = False


    
    
class server_tcp(socketserver.TCPServer):
    """ 
    server_t herda tudo de socketserver.TCPServer, 
    tendo a função de encapsular um servidor TCP 
    """
    

    
    def __init__(args,  **kwargs):
        HOST, PORT = kwargs.get('host', "localhost"), kwargs.get('port', 9999)
        super().__init__((HOST, PORT), MyTCPHandler)
        

 



if __name__ == "__main__":
    print('SERVIDOR ON')
    # Create the server, binding to localhost on port 9999

    server = server_tcp()

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
