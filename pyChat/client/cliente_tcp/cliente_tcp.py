import json
import socket

from pyChat.client.cliente_tcp.async_tcp import client2


class cliente_tcp:
    def __init__(self, controller, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')     # Endereco IP do Servidor
        self.port = kwargs.get('port', 3333)           # Porta que o Servidor está
        self.dest = (self.host, self.port)
        self.con_status = False

        self.controller = controller
        
        self.client_t = client2.ClientProtocol(controller)
        

    def conecta(self):
        if self.con_status == False:
            dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
            try:
                self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcp.connect(self.dest)
                self.con_status = True
                dic_feedback['feedback'] = 0
                return(dic_feedback)
            except Exception as Expt:
                print(Expt)
                print(type(Expt))
                dic_feedback['feedback'] = 1
                dic_feedback['Erro'] = 'falha na conexão'
                dic_feedback['Exception'] = Expt
                print(dic_feedback)
                return(dic_feedback)
                
    def conecta(self):
        try:
            self.client_t.connect()
        except Exception as Expt:

            return Expt


    def desconecta(self):
        if self.con_status == True:
            dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
            try:
                self.tcp.close()
                self.con_status = False
                dic_feedback['feedback'] = 0
                return(dic_feedback)
                
            except Exception as Expt:
                #LEMBRAR DE TRATAR ERROS
                print(Expt)
                print(type(Expt))
                dic_feedback['feedback'] = 1
                dic_feedback['Erro'] = 'Falha na desconexão'
                dic_feedback['Exception'] = Expt
                return(dic_feedback)


    def recebe(self):
        #CASO NAO HAVA CONEXÃO, OU A CONEXÃO NÃO TENHA SIDO ESTABELECIDA:
        dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
        if self.con_status == False:
            self.conecta()
        #ABAIXO UM JEITO ALTERNATIVO DE FAZER A CONVERSÃO:
        #PRECISO VER QUAL É O CORRETO (TO-DO)
        #data = str(self.tcp.recv(4096), "utf-8")
        try:
            dado = self.tcp.recv(11264).decode('utf-8')
            #~ print('Dado recebido do serv: ', dado)
        except Exception as Expt:
            print(Expt, type(Expt))
            dic_feedback['feedback'] = -1
            dic_feedback['Erro'] = 'Erro ao receber dado'
            dic_feedback['Exception'] = Expt
            return(dic_feedback)
        
        try:
            obj = json.loads(dado)
            print(obj)
            return(obj)
        except Exception as Expt:
            print(Expt, type(Expt))
            dic_feedback['feedback'] = -1
            dic_feedback['Erro'] = 'Erro ao codificar o dado'
            dic_feedback['Exception'] = Expt
            return(dic_feedback)


    def envia_req(self, obj):
        try:
            print('Enviando req: ', obj)
            data = json.dumps(obj)
            data.encode()
            #self.client_t.send_message(data)
            self.client_t.transport.write(data.encode('utf-8'))
        except Exception as Expt:
            return Expt

