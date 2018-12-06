from . import sqliteServer
from .DTP import *
from . import Models

class DataMapper(sqliteServer.sqliteConn):
    def __init__(self):
        super().__init__()

    def createTables(self):
        sql = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, userEmail VARCHAR(40) UNIQUE, userName VARCHAR(50), password VARCHAR(6))'
        self.__execute_commit__(sql)

class UserMapper(DataMapper):
    def __init__(self):
        super().__init__()

    def newUser(self, user:Models.user):
        tupl = (user.userName, user.userEmail, user.password)
        sql = 'INSERT INTO users (userName, userEmail, password) VALUES(?, ?, ?);'
        feedback = self.__execute_commit__(sql, tupl)

        if feedback == 0:
            newUser = self.searchUser(user.userEmail)
            tableName = 'friends_' + str(newUser.idd)
            sql = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(id_friend INTEGER UNIQUE, FOREIGN KEY(id_friend) REFERENCES users(id));'
            feedback = self.__execute_commit__(sql)

            if feedback == 0:
                return newUser

            elif isinstance(feedback, Exception):
                return feedback

        elif isinstance(feedback, Exception):
            return feedback


    def login(self, login:Models.Login):
        userEmail = login.userEmail
        password = login.password
        sql = 'SELECT id, password FROM users WHERE userEmail = "' + userEmail + '";'

        tupl = self.__execute_fetchone__(sql)
        if isinstance(tupl, Exception):
            return tupl
        elif tupl is None:
            return Exception('User not found')

        else:
            id_user = tupl[0]
            actualPassword = tupl[1]
            if actualPassword == password:
                return self.retrieveUser(id_user)
            # TODO ROTINAS DE ERROS PASSWORD INVALIDO E USUARIO NAO EXISTENTE.
            else:
                return Exception('Incorrect password')

    def namesLike_old(self, nameLike:str):
        nameLike = nameLike + '%'
        sql = 'SELECT id, userName, userEmail FROM users WHERE userName LIKE "' + nameLike + '" ;'
        lst_tupl = self.__execute_fetchall__(sql)

        lstUser = Models.LstUsers()
        if lst_tupl != []:
            for tupl in lst_tupl:
                user = Models.user()
                user.idd = int(tupl[0])
                user.userName = tupl[1]
                user.userEmail = tupl[2]
                lstUser.append(user)
        return lstUser

    def namesLike(self,user:Models.user, nameLike:str):
        tableName = 'friends_' + str(user.idd)
        nameLike = nameLike + '%'
        sql = 'SELECT ' \
              'id_friend,  ' \
              'userName, u' \
              'serEmail ' \
              'FROM ' + tableName + \
              ' INNER JOIN users ON (' + tableName + '.id_friend = users.id)' \
              ' WHERE userName LIKE "' + nameLike + '" ;'

        lst_tupl = self.__execute_fetchall__(sql)

        lstUser = Models.LstUsers()
        if lst_tupl != []:
            for tupl in lst_tupl:
                user = Models.user()
                user.idd = int(tupl[0])
                user.userName = tupl[1]
                user.userEmail = tupl[2]
                lstUser.append(user)
        return lstUser


    def retrieveUser(self, id_user):
        id_user = self.__strip_id__(id_user, tipo='str')
        sql = 'SELECT userEmail, userName FROM users WHERE id = ' + id_user + ';'
        tupl = self.__execute_fetchone__(sql)

        if tupl != None:
            user = Models.user()
            user.userEmail = tupl[0]
            user.userName = tupl[1]
            user.idd = int(id_user)
            return user
        else:
            return Exception('User not found')

    def searchUser(self, userEmail:str):
        sql = 'SELECT id, userName FROM users WHERE userEmail = "' + userEmail + '" ;'
        tupl = self.__execute_fetchone__(sql)
        if tupl != None:
            user = Models.user()
            user.userEmail = userEmail
            user.userName = tupl[1]
            user.idd = int(tupl[0])
            return user
        else:
            return Exception('User not found')

    def addFriend(self, friendEmail:str, user:Models.user):
        if self.searchUser(friendEmail) != None:
            friend = self.searchUser(friendEmail)
            if isinstance(friend, Exception):
                return friend
            elif friend is None:
                return Exception('User not found')
            else:
                id_friend = friend.idd
                userId = user.idd

                #O contato é adcionado na tabela de amigos do usuário:
                tableName = 'friends_'+str(userId)
                sql = 'INSERT INTO ' + tableName + ' VALUES (' + str(id_friend) + ');'
                feedback = self.__execute_commit__(sql)

                if isinstance(feedback, Exception):
                    return feedback

                # O usuário é adcionado na tabela de amigos do contato:
                tableName = 'friends_'+str(id_friend)
                sql = 'INSERT INTO ' + tableName + ' VALUES (' + str(userId) + ');'
                feedback = self.__execute_commit__(sql)
                print('Era pra ser Except: -> ' + str(type(feedback)))

                if isinstance(feedback, Exception):
                    print('Era pra ser Except: -> ' + str(type(feedback)))
                    return feedback

                #É criada uma tabela de Chat:
                ChatMapper().newChat(userId, id_friend)
                return friend
        else:
            return Exception('User not found')

    def retrieveFriends(self, user:Models.user):
        id_user = user.idd
        tableName = 'friends_' + str(id_user)
        sql = 'SELECT id_friend,  userName, userEmail FROM ' + tableName + ' INNER JOIN users ON (' + tableName + '.id_friend = users.id);'
        lst_tupl = self.__execute_fetchall__(sql)

        if isinstance(lst_tupl, Exception):
            return lst_tupl
        elif lst_tupl is None:
            return Exception('Friends list not found')

        else:
            lstUser = Models.LstUsers()
            for elem in lst_tupl:
                friendUser = Models.user()
                friendUser.idd = int(elem[0])
                friendUser.userName = elem[1]
                friendUser.userEmail = elem[2]
                lstUser.append(friendUser)
            return lstUser

    def dropFriendship(self, id_user1, id_user2):
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'DROP TABLE ' + tableName + ';'
        self.__execute_commit__(sql)

        tableName = 'friends_'+id_user1
        sql = 'DELETE FROM ' + tableName + ' WHERE((id_user1=' + id_user1 + ' AND id_user2=' + id_user2 + ') OR ((id_user1=' + id_user2 + ' AND id_user2= ' + id_user1 + ');'
        self.__execute_commit__(sql)

        tableName = 'friends_' + id_user2
        sql = 'DELETE FROM ' + tableName + ' WHERE((id_user1=' + id_user1 + ' AND id_user2=' + id_user2 + ') OR (id_user1=' + id_user2 + ' AND id_user2= ' + id_user1 + '));'
        self.__execute_commit__(sql)


class ChatMapper(DataMapper):
    def __init__(self):
        super().__init__()

    def newChat(self, id_user1, id_user2):
        # Método cria uma tabela de conversa para dois usários dados.
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_dest INTEGER, id_remete INTEGER, data_hora datetime, conteudo TEXT, FOREIGN KEY(id_dest) REFERENCES users(id), FOREIGN KEY(id_remete) REFERENCES users(id))'
        return self.__execute_commit__(sql)


    def dropChat(self, id_user1, id_user2):
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'DROP TABLE ' + tableName + ';'
        return self.__execute_commit__(sql)

    def retrieveChat(self, userId, friendId):
        # Método que busca a conversa de dois usuários dados
        # Como a tabela foi criada pelo método newChat(), o nome dela respeita a lógica seguinte:
        if int(userId) > int(friendId):
            tableName = 'chat_' + str(userId) + '_' + str(friendId)
        elif int(friendId) > int(userId):
            tableName = 'chat_' + str(friendId) + '_' + str(userId)

        user = UserMapper().retrieveUser(userId)
        friend = UserMapper().retrieveUser(friendId)

        sql = 'SELECT data_hora, conteudo, id_dest, id_remete FROM ' + tableName + ' ORDER BY data_hora;'

        tupl_lst = self.__execute_fetchall__(sql)

        if isinstance(tupl_lst, Exception):
            return tupl_lst
        elif tupl_lst is None:
            return Exception('Chat not found')

        lstMessage = Models.LstMessages()
        # A ROTINA ABAIXO VERIFICA SE NA MENSAGEM EM QUESTÃO, O USUÁRIO REQUISITANTE DA LISTA DE MENSAGENS FOI O DESTINATÁRIO
        # OU REMETENTE, PARA PREENCHER O NOME(STRING) DE FORMA CORRETA, JÁ QUE A RECUPERAÇÃO DO MESMO VIA INNER JOIN É INVIÁVEL
        # POIS AMBOS RESIDEM NA MESMA TABELA
        for elem_tupl in tupl_lst:
            if userId == int(elem_tupl[3]):
                message = Models.Message()
                message.dateTime = elem_tupl[0]
                message.content = elem_tupl[1]
                message.recipUser = friend
                message.senderUser = user # USUÁRIO REQUISITANTE DO MÉTODO FOI O REMETENTE
                lstMessage.append(message)
            if userId == int(elem_tupl[2]):
                message = Models.Message()
                message.dateTime = elem_tupl[0]
                message.content = elem_tupl[1]
                message.recipUser = user    # USUÁRIO REQUISITANTE DO MÉTODO FOI O DESTINATÁRIO
                message.senderUser = friend
                lstMessage.append(message)
        return lstMessage

    def insertMessage(self, message:Models.Message):
        data_hora = message.dateTime
        conteudo = message.content
        id_user1 = message.senderId
        id_user2 = message.recipId
        tupla_sql = (conteudo, data_hora, id_user2, id_user1)

        if int(id_user1) > int(id_user2):
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif int(id_user2) > int(id_user1):
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)

        sql = 'INSERT INTO '+tableName+' (conteudo, data_hora, id_dest, id_remete) VALUES(?, ?, ?, ?)'
        feedback = self.__execute_commit__(sql, tupla_sql)
        if feedback == 0:
            print("mensagem salva no banco de dados!")
            # APÓS SER SALVA, O STATUS DE ENVIO DA MENSAGEM É ATUALIZADO ABAIXO
            message.statusRecv = 1
            return message
        elif isinstance(feedback, Exception):
            return feedback



class NotificationsMapper(DataMapper):
    def __init__(self):
        super().__init__()