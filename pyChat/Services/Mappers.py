import datetime
from pyChat.Models import Models
from pyChat.servidor.ServerPacks import SqliteServer


class DataMapper(SqliteServer.sqliteConn):
    def __init__(self):
        super().__init__()
        sql1 = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, userEmail VARCHAR(40) UNIQUE, userName VARCHAR(50), password VARCHAR(6), registerDate DATETIME);'
        sql2 = 'CREATE TABLE IF NOT EXISTS notifications_types(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(40) UNIQUE);'
        self.__execute_transaction__(sql1+sql2)

    def createDatabase(self):
        pass


class UserMapper(DataMapper):
    def __init__(self):
        super().__init__()


    def newUser(self, user:Models.user)->Models.user or Exception:
        tupla = ( user.userName , str(user.userEmail) , str(user.password), user.registerDate)
        #sql1 = 'INSERT INTO users (userName, userEmail, password) VALUES (' + str(user.userName) + ', ' + str(user.userEmail) + ', ' + str(user.password) + ');'
        sql1 = 'INSERT INTO users (userName, userEmail, password, registerDate) VALUES (?, ?, ?, ?);'
        self.__execute_commit__(sql1, tupla)

        newUser = self.searchUser(user.userEmail)

        tableFriends = 'friends_' + str(newUser.idd)
        tableNotifications = 'notifications_' + str(newUser.idd)
        tableBlocks = 'blocks_' + str(newUser.idd)
        tableNotShowNotfications = 'notShowNotfications_'+str(newUser.idd)
        sql2 = 'CREATE TABLE IF NOT EXISTS ' + tableFriends + '(id_friend INTEGER UNIQUE, confirmation INTEGER, showNotification INTEGER, dateAdd DATETIME, FOREIGN KEY(id_friend) REFERENCES users(id));'
        sql3 = 'CREATE TABLE IF NOT EXISTS ' + tableNotifications + '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_type INTEGER, statusRead INTEGER, registerDate DATETIME, FOREIGN KEY(id_type) REFERENCES notifications(id));'
        sql4 = 'CREATE TABLE IF NOT EXISTS ' + tableNotShowNotfications + '(id_type INTEGER, FOREIGN KEY(id_type) REFERENCES notifications(id));'
        sql5 = 'CREATE TABLE IF NOT EXISTS ' + tableBlocks + '(id_block INTEGER UNIQUE, registerDate DATETIME, FOREIGN KEY(id_block) REFERENCES users(id));'
        commitFeedback = self.__execute_transaction__(sql2+sql3+sql4+sql5)

        if commitFeedback == 0:
            return newUser
        elif isinstance(commitFeedback, Exception):
            return commitFeedback



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
        commitFeedback = self.__execute_fetchone__(sql)
        if isinstance(commitFeedback, Exception):
            return commitFeedback

        elif commitFeedback != None:
            user = Models.user()
            user.userEmail = userEmail
            user.userName = commitFeedback[1]
            user.idd = int(commitFeedback[0])
            return user
        else:
            return Exception('Usuário não encontrado!')

    def friendshipAcepted(self, friendship:Models.Friendship):
        senderUserId = friendship.senderUser.idd
        recipUserId = friendship.recipUser.idd

        tableSender = 'friends_' + str(senderUserId)
        tableRecip = 'friends_' + str(recipUserId)

        sql1 = 'UPDATE '+tableSender+' SET CONFIRMATION = 1 WHERE id_friend = '+recipUserId+';'
        sql2 = 'UPDATE ' + tableRecip + ' SET CONFIRMATION = 1 WHERE id_friend = '+senderUserId+';'

        commitFeedback = self.__execute_transaction__(sql1+sql2)
        if commitFeedback == 0:
            return friendship
        elif isinstance(commitFeedback, Exception):
            return commitFeedback


    def addFriend(self, senderUser:Models.user, friendEmail:str) -> Models.Friendship or Exception:
        if self.searchUser(friendEmail) != None:
            recipUser = self.searchUser(friendEmail)
            if isinstance(recipUser, Exception):
                return recipUser
            elif recipUser is None:
                return Exception('Usuário não encontrado!')
            else:
                senderId = senderUser.idd
                recipId = recipUser.idd
                tableBlocks = 'blocks_' + str(recipId)
                sql = 'SELECT id_block FROM '+tableBlocks+' WHERE id_block = '+str(senderId)+';'
                id = self.__execute_fetchone__(sql)
                # VERIFICA SE O REMETENTE DO PEDIDO DE AMIZADO ESTÁ BLOQUEADO PELO DESTINATÁRIO
                if id == None or id == 0:
                    registerDate = datetime.datetime.now()
                    # O contato é adcionado na tabela de amigos do usuário:
                    tableName1 = 'friends_' + str(senderId)
                    tableName2 = 'friends_' + str(recipId)
                    sql1 = 'INSERT INTO ' + tableName1 + '(id_friend, confirmation, showNotification) VALUES (' + str(
                        recipId) + ', 0, 1);'
                    sql2 = 'INSERT INTO ' + tableName2 + '(id_friend, confirmation, showNotification) VALUES (' + str(
                        senderId) + ', 0, 1);'

                    if recipId > senderId:
                        tableName = 'chat_' + str(recipId) + '_' + str(senderId)
                    elif senderId > recipId:
                        tableName = 'chat_' + str(senderId) + '_' + str(recipId)

                    sql3 = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_dest INTEGER, id_remete INTEGER, data_hora datetime, conteudo TEXT, statusRead INTEGER, statusReceived INTEGER, FOREIGN KEY(id_dest) REFERENCES users(id), FOREIGN KEY(id_remete) REFERENCES users(id));'

                    commitFeedback = self.__execute_transaction__(sql1 + sql2 + sql3)
                    print('commitFeedback ' + str(commitFeedback))
                    if commitFeedback == 0:
                        friendship = Models.Friendship(senderUser, recipUser)
                        return friendship
                    elif isinstance(commitFeedback, Exception):
                        return commitFeedback
                elif int(id) == senderId:
                    #CASO CONSTE NA LISTA DE BLOQUEIOS:
                    return Exception('Usuário não encontrado!')
        else:
            return Exception('Usuário não encontrado!')


    def retrieveFriends(self, user:Models.user):
        id_user = user.idd
        tableName = 'friends_' + str(id_user)
        sql = 'SELECT id_friend,  userName, userEmail, showNotification, dateAdd FROM ' + tableName + ' INNER JOIN users ON (' + tableName + '.id_friend = users.id);'
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
                friendUser.showNotification = elem[3]
                friendUser.dateAdd = elem[4]
                lstUser.append(friendUser)
            return lstUser

    def dropFriendship(self, friendship:Models.Friendship):
        id_user1 = friendship.senderUser.idd
        id_user2 = friendship.recipUser.idd

        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'DROP TABLE ' + tableName + ';'
        self.__execute_commit__(sql)

        tableName1 = 'friends_'+id_user1
        sql1 = 'DELETE * FROM '+tableName+' WHERE(id_friend='+id_user2+');'
        tableName2 = 'friends_'+id_user2
        sql2 = 'DELETE * FROM '+tableName+' WHERE(id_friend=' + id_user1+');'
        commitFeedback = self.__execute_transaction__(sql1+sql2)
        if commitFeedback == 0:
            friendship.accepted = 0
            return friendship
        elif isinstance(commitFeedback, Exception):
            return commitFeedback

    def deleteMessage(self, message:Models.Message):
        id_user1 = message.senderUser.idd
        id_user2 = message.recipUser.idd
        messageId = message.idd
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'DELETE * FROM ' + tableName + 'WHERE id = '+str(messageId)+';'
        commitFeedback = self.__execute_commit__(sql)

        if commitFeedback == 0:
            message.content = ''
            return message
        elif isinstance(commitFeedback, Exception):
            return commitFeedback

    def deleteChat(self, friendship: Models.Friendship):
        id_user1 = friendship.senderUser.idd
        id_user2 = friendship.recipUser.idd
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'DELETE * FROM ' + tableName + ';'
        commitFeedback = self.__execute_commit__(sql)
        if commitFeedback == 0:
            return friendship
        elif isinstance(commitFeedback, Exception):
            return commitFeedback

    def blockUser(self, friendship:Models.Friendship):
        senderId = friendship.senderUser.idd
        recipId = friendship.recipUser.idd
        commitFeedback = self.dropFriendship(friendship)
        registerDate = datetime.datetime.now()
        if isinstance(commitFeedback, Models.Friendship):
            # CASO O COMMIT TENHA DADO CERTO:
            tableBlocks = 'blocks_' + str(senderId.idd)
            sql = 'INSERT INTO ' + tableBlocks + '(id_block) VALUES ('+str(recipId)+');'
            commitFeedback = self.__execute_commit__(sql)
            if commitFeedback == 0:
                friendship.accepted = 0
                friendship.blocked = 1
                return friendship
            elif isinstance(commitFeedback, Exception):
                return commitFeedback
        elif isinstance(commitFeedback, Exception):
            return commitFeedback

class ChatMapper(DataMapper):
    def __init__(self):
        super().__init__()

    def newChat(self, id_user1, id_user2):
        # Método cria uma tabela de conversa para dois usários dados.
        if id_user1 > id_user2:
            tableName = 'chat_' + str(id_user1) + '_' + str(id_user2)
        elif id_user2 > id_user1:
            tableName = 'chat_' + str(id_user2) + '_' + str(id_user1)
        sql = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_dest INTEGER, id_remete INTEGER, data_hora datetime, conteudo TEXT, statusRead INTEGER, statusReceived INTEGER, FOREIGN KEY(id_dest) REFERENCES users(id), FOREIGN KEY(id_remete) REFERENCES users(id))'
        return self.__execute_commit__(sql)

    def retrieveChat(self, friendship: Models.Friendship):
        # PRIMEIRO É VERIFICADO SE O PEDIDO DE AMIZADE FOI ACEITO
        tableFriends = 'friends_' + str(friendship.senderUser.idd)
        sql = 'SELECT confirmation FROM '+tableFriends+ ' WHERE id_friend = '+str(friendship.recipUser.idd)+';'
        confirmation = self.__select_fetchone__(sql)
        if int(confirmation[0]) == 1:
            userId = friendship.senderUser.idd
            friendId = friendship.recipUser.idd
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
        else:
            #CASO O PEDIDO DE AMIZADE AINDA NÃO TENHA SIDO ACEITO PELO DESTINATÁRIO:
            lstMessage = Models.LstMessages()
            #O MÉTODO RETORNA UMA LISTA VAZIA:
            return lstMessage

    def insertMessage(self, message:Models.Message):


        senderId = message.senderUser.idd
        recipId = message.recipUser.idd

        # VERIFICA SE O REMETENTE DA MENSAGEM ESTÁ BLOQUEADO PELO DESTINATÁRIO
        # VERIFICAÇÃO REDUNTANTE
        tableBlocks = 'blocks_' + str(recipId)
        sql = 'SELECT id_block FROM ' + tableBlocks + ' WHERE id_block = ' + str(senderId) + ';'
        idd = self.__execute_fetchone__(sql)
        # CASO O REMETENTE NÃO ESTEJA BLOQUEADO
        if idd == None:
            data_hora = message.dateTime
            conteudo = message.content
            statusRead = message.statusRead
            statusReceived = message.statusRecv
            senderId = message.senderUser.idd
            recipId = message.recipUser.idd
            print(senderId, recipId )
            tupla_sql = (conteudo, data_hora, recipId, senderId, statusRead, statusReceived)
            if int(senderId) > int(recipId):
                tableName = 'chat_' + str(senderId) + '_' + str(recipId)
            elif int(recipId) > int(senderId):
                tableName = 'chat_' + str(recipId) + '_' + str(senderId)

            sql = 'INSERT INTO '+tableName+' (conteudo, data_hora, id_dest, id_remete, statusRead, statusReceived) VALUES(?, ?, ?, ?, ?, ?);'
            feedback = self.__execute_commit__(sql, tupla_sql)
            if feedback == 0:
                print("mensagem salva no banco de dados!")
                # APÓS SER SALVA, O STATUS DE ENVIO DA MENSAGEM É ATUALIZADO ABAIXO
                message.statusRecv = 1
                return message
            elif isinstance(feedback, Exception):
                return feedback
        elif int(idd) == senderId:
            raise Exception('Usuário remetente está bloqueado!')



class NotificationsMapper(DataMapper):
    def __init__(self):
        super().__init__()