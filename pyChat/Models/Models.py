from datetime import datetime


class AppModel:
    def __init__(self):
        self._idd = -1

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, idd):
        if type(idd) != int:
            try:
                idd = int(idd)
                self._idd = idd
            except Exception as Expt:
                raise Expt
        else:
            self._idd = idd

    def __str__(self):
        return 'isto nao é um dicionario ' + str(dict(self))

    def __repr__(self):
        return str(dict(self))

    def toJson(self):
        pass

    def fromJson(self, obj: dict):
        pass


class Message(AppModel):
    """LEMBRAR QUE O datetime nao é serializável pelo JSON"""

    def __init__(self):
        super().__init__()

        self.sessionUserId = -1

        self.isoformat = '%Y-%m-%d %H:%M:%S.%f'
        self._dateTime = ''
        self._senderUser = user()
        self._recipUser = user()
        self.content = ''
        self.statusRecv = False
        self.statusRead = False

    def toJson(self):
        dictJson = {}
        dictJson['idd'] = self._idd
        dictJson['dateTime'] = self.dateTime.isoformat(' ')
        dictJson['senderUser'] = self._senderUser.toJson()
        dictJson['recipUser'] = self._recipUser.toJson()
        dictJson['content'] = self.content
        dictJson['statusRecv'] = self.statusRecv
        dictJson['statusRead'] = self.statusRead
        return dictJson

    def fromJson(self, dictJson: dict):
        self._idd = dictJson['idd']
        self._dateTime = datetime.strptime(dictJson['dateTime'], self.isoformat)
        self._senderUser = user().fromJson(dictJson['senderUser'])
        self._recipUser = user().fromJson(dictJson['recipUser'])
        self.content = dictJson['content']
        self.statusRecv = dictJson['statusRecv']
        self.statusRead = dictJson['statusRead']
        return self

    @property
    def dateTime(self):
        return self._dateTime

    @dateTime.setter
    def dateTime(self, DateTime):
        if type(DateTime) is str:
            try:
                self._dateTime = datetime.strptime(DateTime, self.isoformat)
            except Exception as Expt:
                raise Expt
        elif type(DateTime) is datetime:
            self._dateTime = DateTime
        else:
            raise Exception('Erro ao atribuir a dataHora da mensagem.')

    @property
    def recipUser(self):
        return self._recipUser

    @recipUser.setter
    def recipUser(self, recipUser):
        if isinstance(recipUser, user):
            self._recipUser = recipUser
        else:
            raise Exception('Precisa ser do tipo User')

    @property
    def senderName(self):
        return self._senderUser.userName

    @property
    def senderEmail(self):
        return self._senderUser.userEmail

    @property
    def senderId(self):
        return self._senderUser.idd

    @property
    def recipName(self):
        return self._recipUser.userName

    @property
    def recipEmail(self):
        return self._recipUser.userEmail

    @property
    def recipId(self):
        return self._recipUser.idd

    @property
    def senderUser(self):
        return self._recipUser

    @senderUser.setter
    def senderUser(self, senderUser):
        if isinstance(senderUser, user):
            self._senderUser = senderUser
        else:
            raise Exception('Precisa ser do tipo User')

    def __setHora__(self):
        pass

    def __iter__(self):
        yield 'dateTime', self.dateTime.isoformat(' ')
        yield 'idd', self._idd
        yield 'senderUser', dict(self.senderUser)
        yield 'recipUser', dict(self.recipUser)
        yield 'content', self.content
        yield 'statusRecv', self.statusRecv
        yield 'statusRead', self.statusRead
        #yield 'sessionUserId', self._sessionUserId

    def __str__(self):
        return str(dict(self))

    def __eq__(self, obj):
        return (self.dateTime == obj.dateTime)

    def __ne__(self, obj):
        return (self.dateTime != obj.dateTime)

    def __lt__(self, obj):
        return (self.dateTime < obj.dateTime)

    def __le__(self, obj):
        return (self.dateTime <= obj.dateTime)

    def __gt__(self, obj):
        return (self.dateTime > obj.dateTime)

    def __ge__(self, obj):
        return (self.dateTime >= obj.dateTime)

    def __repr__(self):
        return str(dict(self))

    def toTreeview(self):
        try:
            elem1 = str(self.senderName) + ' - ' + str(self.dateTime.day) + '/' + str(self.dateTime.month) + '/' + str(
                self.dateTime.year) + ' às ' + str(self.dateTime.hour) + ':' + str(self.dateTime.minute)
        except:
            elem1 = str(self.senderName) + ' - ' + str(self.dateTime.day) + '/' + str(self.dateTime.month) + '/' + str(
                self.dateTime.year) + ' às ' + str(self.dateTime.hour) + ':' + str(self.dateTime.minute)

        elem2 = self.content
        dic_treeView = {'text': elem1, 'values': [elem2], 'index': 'end'}
        return dic_treeView


class user(AppModel):
    def __init__(self):
        """

        :rtype: object
        """
        super().__init__()
        self.tipo = self.__class__.__name__
        self._userName = 'User Name'
        self._password = 123456
        self._idd = -1
        self._userEmail = 'user@null.com'

    def toJson(self):
        dictJson = {}
        dictJson['idd'] = self._idd
        dictJson['userName'] = self._userName
        dictJson['userEmail'] = self._userEmail
        dictJson['password'] = self._password
        return dictJson

    def fromJson(self, dictJson: dict):
        self._idd = dictJson['idd']
        self._userName = dictJson['userName']
        self._userEmail = dictJson['userEmail']
        self._password = dictJson['password']
        return self

    def toTreeview(self):
        dictTreeview = {'idd': self._idd, 'text': self._userName, 'values': ['']}
        return dictTreeview

    def __iter__(self):
        yield 'userName', self._userName
        yield 'userEmail', self._userEmail
        yield 'password', self._password
        yield 'idd', self._idd

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, idd):
        print(idd)
        if type(idd) != int:
            try:
                idd = int(idd)
                self._idd = idd
            except Exception as Expt:
                raise Expt
        else:
            self._idd = idd

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, name):
        self._userName = name

    @property
    def password(self):
        return self._password

    @property
    def userEmail(self):
        return self._userEmail

    @userEmail.setter
    def userEmail(self, userEmail):
        self._userEmail = userEmail

    @password.setter
    def password(self, password):
        password = str(password)
        if type(password) == str:
            if len(password) > 6:
                raise Exception('Senha muito longa!')
            elif len(password) < 3:
                raise Exception('Senha muito curta!')
            else:
                self._password = password
        else:
            raise Exception('Senha deve ser tipo String.')

class Friendship(AppModel):
    def __init__(self, senderUser: user = user(), recipUser: user = user()):
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser
        self.blocked = 0
        self.accepted = 0

    def toJson(self):
        dictJson = {'senderUser': self.senderUser.toJson(),
                    'recipUser': self.recipUser.toJson(),
                    'blocked': self.blocked,
                    'accepted': self.accepted}
        return dictJson

    def fromJson(self, dictJson: dict):
        self.senderUser = user().fromJson(dictJson['senderUser'])
        self.recipUser = user().fromJson(dictJson['recipUser'])
        self.blocked = dictJson['blocked']
        self.accepted = dictJson['accepted']
        return self

class Login(AppModel):
    def __init__(self):
        super().__init__()
        self.userEmail = ''
        self.password = None

    def __iter__(self):
        yield 'userEmail', self.userEmail
        yield 'password', self.password

    def toJson(self):
        dictJson = {}
        dictJson['userEmail'] = self.userEmail
        dictJson['password'] = self.password
        return dictJson

    def fromJson(self, dictJson: dict):
        self.password = dictJson['password']
        self.userEmail = dictJson['userEmail']
        return self


class LstUsers(list):
    """
    A PRESENTE CLASSE RECEBE UMA LISTA DE DICIONARIOS REPRESENTANDO MENSAGENS
    EM SEGUIDA PERCORRE A LISTA DE DICIONÁRIOS E INSTANCIA AS MENSAGENS POR MEIO DOS DICONARIOS
    OU SEJA, O CONSTRUTOR DA CLASSE MENSAGEM RECEBE COMO PARAMETRO UM DICIONARIO COM OS ATRIBUTOS
    """

    def __init__(self):
        super().__init__()

    def toJson(self):
        lstJson = []
        for elem in self:
            lstJson.append(elem.toJson())
        return lstJson

    def fromJson(self, lstUser: list):
        for dic_elem in lstUser:
            userAux = user().fromJson(dic_elem)
            self.append(userAux)
        return self

    def append(self, object):
        if isinstance(object, user):
            super().append(object)
        else:
            raise Exception('Precisa ser do tipo User')

    def searchId(self, idd):
        for elemUser in self:
            if type(idd) != int:
                idd = int(idd)
            if elemUser.idd == idd:
                return elemUser

    def toTreeview(self):
        lst_treeview = []
        try:
            for elem in self:
                dic_aux = elem.toTreeview()
                lst_treeview.append(dic_aux)
            return (lst_treeview)
        except Exception as Expt:
            print(Expt)


class LstMessages(list):
    """
    A PRESENTE CLASSE RECEBE UMA LISTA DE DICIONARIOS REPRESENTANDO MENSAGENS
    EM SEGUIDA PERCORRE A LISTA DE DICIONÁRIOS E INSTANCIA AS MENSAGENS POR MEIO DOS DICONARIOS
    OU SEJA, O CONSTRUTOR DA CLASSE MENSAGEM RECEBE COMO PARAMETRO UM DICIONARIO COM OS ATRIBUTOS
    """

    def __init__(self):
        super().__init__()

    def append(self, object):
        if isinstance(object, Message):
            super().append(object)
        else:
            raise Exception('Precisa ser do tipo Message')

    def toJson(self):
        lstJson = []
        for elem in self:
            lstJson.append(elem.toJson())
        return lstJson

    def fromJson(self, lstMessage):
        if lstMessage != []:
            for elem in lstMessage:
                print(elem)
                messageAux = Message().fromJson(elem)
                self.append(messageAux)
            return self
        else:
            return self

    def toTreeview(self):
        try:
            lst_treeview = []
            for elem in self:
                dic_aux = elem.toTreeview()
                lst_treeview.append(dic_aux)
            #lst_treeview.reverse()
            return lst_treeview
        except Exception as Expt:
            print(Expt)