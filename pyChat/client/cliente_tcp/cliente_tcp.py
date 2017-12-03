import socket
import json


class cliente_tcp:
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')     # Endereco IP do Servidor
        self.port = kwargs.get('port', 3333)           # Porta que o Servidor está
        self.dest = (self.host, self.port)
        self.con_status = False

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




