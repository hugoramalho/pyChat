import sqlite3


class conexao_BD_prog:

    def __init__(self):
        try:
            pass
            #O BD já está criado! NÃO DESCOMENTAR O MÉTODO:
            #self.__cria_BD__()

            self.conn = sqlite3.connect("bd_server\BD_prog.db")
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            #self.data = self.cursor.fetchone()
            self.conn.close()
            self.con_status = False
    
        except Exception as Expt:
            self.__expt_msg__(Expt)
            pass


    def __conect_BD__(self):
        try:
            if(self.con_status == False):
                self.conn = sqlite3.connect("bd_server\BD_prog.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()

            else:
                raise Exception('Conexão indisponível ou já em uso')
                pass
        except Exception as Expt:
            self.__expt_msg__(Expt)


    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()


    def __select_fetchone__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __lastrowid__(self):
        return(self.cursor.lastrowid)
        

    def __execute_fetchone__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)



    def __select_fetchall__(self, sql,  tpl = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)


    def __execute_fetchall__(self, sql,  tpl = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)
            
            

    def __execute_commit__(self, sql = '', tpl  = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(0)
        
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __strip_id__(self, idd, tipo = 'int'):
        idd = str(idd)
        idd = idd.strip(')').strip( '(' ).strip( "," )
        
        if tipo == 'int':
            idd = int(idd)
            return(idd)
        elif tipo == 'str':
            return(idd)
        else:
            raise Exception('Argumento: ', tipo, ' não reconhecido, precisa ser "str" ou "int"')

    def finaliza_conexao(self):
        self.__disconect_BD__()

    def __expt_msg__(self, Expt):
        print('Erro no BD')
        self.finaliza_conexao()
        print(str(Expt))
        print(type(Expt))
        return(Expt)

    def __cria_BD__(self):
        # CRIANDO A TABELA mensagens:
        sql = 'CREATE TABLE IF NOT EXISTS mensagens(id INTEGER PRIMARY KEY AUTOINCREMENT, recipId INTEGER, id_remete INTEGER, dateTime datetime, content TEXT, FOREIGN KEY(recipId) REFERENCES usuarios(id), FOREIGN KEY(id_remete) REFERENCES usuarios(id))'
        self.__execute_commit__(sql)

        # CRIANDO A TABELA usuarios:
        sql = 'CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(40) UNIQUE, senha VARCHAR(6))'
        self.__execute_commit__(sql)

####################################################################
# MÉTODOS DE INSERÇÃO:

    def insere_user(self, **kwargs):
        print(kwargs)
        tupla = (kwargs.get('userName'), kwargs.get('password'))

        sql = 'INSERT INTO usuarios (nome, senha) VALUES(?, ?)'
        feedback = self.__execute_commit__(sql, tupla)
        dic_feedback = {}
        
        if feedback != 0:
            dic_feedback['feedback'] = 1
            dic_feedback['Erro'] = 'usuario ja cadastrado'
        else:
            dic_feedback['feedback'] = 0
            dic_feedback['Erro'] = ''
            print('usuario salvo no banco de dados!')
        return(dic_feedback)

    def insere_msg(self, **kwargs):
        data_hora = kwargs.get('dateTime')
        conteudo = kwargs.get('content')
        id_dest = str(kwargs.get('recipId'))
        id_remete = str(kwargs.get('senderId'))
        tupla_sql = (conteudo, data_hora, id_dest, id_remete)

        sql = 'INSERT INTO mensagens (content, dateTime, recipId, id_remete) VALUES(?, ?, ?, ?)'
        self.__execute_commit__(sql, tupla_sql)
        
        # LEMBRAR QUE FEEDBACK PRECISA SER IMPlwMENTANDO PARA TRATAR ERROS
        feedback = {}
        feedback['feedback'] = 0
        print("mensagem salva no banco de dados!")
        return(feedback)


#########################################################################
# MÉTODOS DE COLETA: (FETCH)

    def fetch_usuario(self, nome):      
        sql = 'SELECT id, nome, senha FROM usuarios WHERE nome = "' + nome + '" ;'
        tupl = self.__execute_fetchone__(sql)
        
        dic_return = {}
        if tupl != None:
            dic_return = {}
            dic_return['feedback'] = 0
            dic_return['id_user'] = tupl[0] 
            dic_return['nome_user'] = tupl[1]
            dic_return['senha'] = tupl[2]
        else:
            dic_return['feedback'] = 1
            dic_return['Erro'] = 'usuario nao encontrado'
        return(dic_return)

    def fetchall_contatos_like(self, **kwargs):
        nome_like = kwargs.get('nome_like')
        nome_like = nome_like + '%'
        sql = 'SELECT id, nome FROM usuarios WHERE nome LIKE "' + nome_like + '" ;'
        #~ print(sql)
        lst_tupl = self.__execute_fetchall__(sql)
        #~ print(lst_tupl)

        dic_return = {}
        lst_contat =[]
        if lst_tupl != []:
            dic_return['feedback'] = 0
            for tupl in lst_tupl:
                #~ print(tupl)
                #~ print(type(tupl))
                #~ print(tupl[0])
                dic_elem = {}
                dic_elem['id_contato'] = tupl[0]
                dic_elem['nome_contato'] = tupl[1]
                lst_contat.append(dic_elem)
            dic_return['lst_contatos'] = lst_contat
        else:
            dic_return['feedback'] = 1
            dic_return['Erro'] = 'usuario nao encontrado'
        return(dic_return)

    def fetchall_contatos(self, id_user):
        id_user = self.__strip_id__(id_user, 'str')
        
        sql = 'SELECT id, nome FROM usuarios WHERE id != ' + id_user
        lst_tupl = self.__execute_fetchall__(sql)
        
        lst_dic = []
        for elem in lst_tupl:
            dic_elem = {}
            dic_elem['id_contato'] = elem[0]
            dic_elem['nome_contato'] = elem[1]
            lst_dic.append(dic_elem)
        return(lst_dic)
        

    def fetch_mensagens(self, id_user, id_contato):
        id_user = self.__strip_id__(id_user, tipo = 'str')
        sql = 'SELECT nome FROM usuarios WHERE id = ' + id_user + ';'
        nome_user = self.__execute_fetchall__(sql)
        #~ print(nome_user)
        
        id_contato = self.__strip_id__(id_contato, tipo = 'str')
        sql = 'SELECT nome FROM usuarios WHERE id = ' + id_contato + ';'
        nome_contato = self.__execute_fetchall__(sql)
        #~ print(nome_contato)

        sql = 'SELECT dateTime, content, recipId, id_remete, nome FROM mensagens INNER JOIN usuarios ON (mensagens.recipId = usuarios.id) WHERE ((id_remete = '+ id_user +' AND recipId = '+id_contato+') OR (id_remete = '+id_contato+' AND recipId = '+id_user+')) ORDER BY dateTime'
        tupl_lst = self.__execute_fetchall__(sql)
        #~ print(tupl_lst)
       
        lst_dic = []
        for elem_tupl in tupl_lst:
            if  id_user == str(elem_tupl[3]):
                dic_mensg = {}
                dic_mensg['id_user'] = id_user
                dic_mensg['dateTime'] = elem_tupl[0]
                dic_mensg['content'] = elem_tupl[1]
                dic_mensg['recipId'] = elem_tupl[2]
                #dic_mensg['senderId'] = elem_tupl[3]
                dic_mensg['recipName'] = nome_contato[0][0] #NOME DO DESTINATÁRIO
                dic_mensg['senderName'] = nome_user[0][0]
                dic_mensg['senderId'] = id_user
                lst_dic.append(dic_mensg)
            if id_user == str(elem_tupl[2]):
                dic_mensg = {}
                dic_mensg['id_user'] = id_user
                dic_mensg['dateTime'] = elem_tupl[0]
                dic_mensg['content'] = elem_tupl[1]
                dic_mensg['recipId'] = elem_tupl[2]
                #dic_mensg['senderId'] = elem_tupl[3]
                dic_mensg['recipName'] = nome_user[0][0] #NOME DO DESTINATÁRIO
                dic_mensg['senderName'] = nome_contato[0][0]
                dic_mensg['senderId'] = id_contato
                lst_dic.append(dic_mensg)
        return(lst_dic)


######################################################################
######################################################################
# MÉTODOS DE EXCLUSÃO: (DROP)

''' 
  NAO DEU TEMPO DE DESENVOLVER FUNÇÕES DE EXCLUSÃO
'''



#######################################################################
#######################################################################
# MÉTODOS DE MODIFICAÇÃO: (UPDATE)

''' 
   NAO DEU TEMPO DE DESENVOLVER FUNÇÕES DE MODIFICAÇÃO
'''

