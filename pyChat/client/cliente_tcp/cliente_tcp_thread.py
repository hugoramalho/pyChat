import time
import socket
import json
import threading


class cliente_tcp:
    
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')     # Endereco IP do Servidor
        self.port = kwargs.get('port', 3333)           # Porta que o Servidor está
        
        self.dest = (self.host, self.port)
        self.con_status = True
        
        
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect(self.dest)
        
        
        self.ouve_serv = threading.Thread(target = self.client_handler())
        self.ouve_serv.start()
        
        
    def conecta(self):
        if self.con_status == False:
            dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
            #~ try:
                #~ self.con_status = True
                #~ dic_feedback['req'] = 'conexao'

                #~ dic_feedback = json.dumps(dic_feedback)
                #~ dic_feedback = dic_feedback.encode('utf_8')
                #~ self.tcp.sendall(dic_feedback)
                
                #~ dic_feedback = self.recebe()
                #~ if dic_feedback['feedback'] == 0:
                    
                    #~ return(dic_feedback)
                
                #~ else:
                    #~ return(dic_feedback)   
        


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

    
    def client_handler(self):
        #CASO NAO HAVA CONEXÃO, OU A CONEXÃO NÃO TENHA SIDO ESTABELECIDA:
        dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
        #~ if self.con_status == False:
            #~ self.conecta()
        #ABAIXO UM JEITO ALTERNATIVO DE FAZER A CONVERSÃO:
        #PRECISO VER QUAL É O CORRETO (TO-DO)
        #data = str(self.tcp.recv(4096), "utf-8")
        while 1:
            try:
                dado = self.tcp.recv(11264).decode('utf-8')
                print('Dado recebido do serv: ', dado)

            except Exception as Expt:
                print(Expt, type(Expt))
                dic_feedback['feedback'] = -1
                dic_feedback['Erro'] = 'Erro ao receber dado'
                dic_feedback['Exception'] = Expt
                # Envia o dado recebido para recebe_req()
                self.recebe(dic_feedback)
            
            try:
                obj = json.loads(dado)
                print(obj)
                # Envia o dado recebido para recebe_req()
                self.recebe(obj)
                
                
            except Exception as Expt:
                print(Expt, type(Expt))
                dic_feedback['feedback'] = -1
                dic_feedback['Erro'] = 'Erro ao codificar o dado'
                dic_feedback['Exception'] = Expt
                # Envia o dado recebido para recebe_req()
                self.recebe(dic_feedback)




    def recebe(self, dic_com):
        try:
            req = dic_com['req']
            if req != '_envio_msg':
                return(dic_com)
            else:
                pass

        except Exception as Expt:
            print(Expt, type(Expt))

    


    def envia_req(self, obj):
        dic_feedback = {'feedback': 0,'Erro': '', 'Aviso': '', 'Exception': None}
        if self.con_status == False:
            # Abaixo, dic_feedback recebe o feedback da conexão:
            dic_feedback = self.conecta()
            # Se o feedback for algum diferente de 0, houve um erro.
            if dic_feedback['feedback'] != 0:
                # O método é interrompido e retorna o dic_feedback contendo o erro a ser tratado
                return(dic_feedback)
        
        #En seguida tentamos codificar em bytes a mensagem:
        try:
            data = json.dumps(obj)
            #ABAIXO UM JEITO ALTERNATIVO DE FAZER A CONVERSÃO:
            #PRECISO VER QUAL É O CORRETO (TO-DO)
            #data = tcp.sendall(bytes(data, "utf-8"))            
            data_byte = data.encode('utf_8')
        # Caso um erro ocorra, a exceção é capturada:
        except Exception as Expt:
            print(Expt, type(Expt))
            dic_feedback['feedback'] = -1
            dic_feedback['Erro'] = 'Erro ao codificar o dado'
            dic_feedback['Exception'] = Expt
            return(dic_feedback)
        
        #Finalmente tentamos enviar a mensagem para o servidor:=
        try:
            self.tcp.sendall(data_byte)
            # A resposta do servidor é capturada e enviada:
            dic_feedback = self.recebe()
            return(dic_feedback)
        except Exception as Expt:
            print(Expt, type(Expt))
            dic_feedback['feedback'] = 1
            dic_feedback['Erro'] = 'Erro ao enviar o dado'
            dic_feedback['Exception'] = Expt
            return(dic_feedback)




