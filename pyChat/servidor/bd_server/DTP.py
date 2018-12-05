from . import Models

class InternalExceptions:
    def __init__(self, requestName, exception: Exception):
        self.requestName = requestName
        self.errorName = str(exception)
        self.exception = 1

    def toJson(self):
        dictJson = {'request': self.requestName, 'errorName': self.errorName, 'exception': self.exception}
        return dictJson


class DataTransfer:
    def __init__(self):
        self.requestName = ''
        self.exception = 0
        pass

    def toJson(self):
        pass

    def fromJson(self, dictObj: dict):
        pass


class Request(DataTransfer):
    def __init__(self, requestName, data: Models.AppModel or list):
        super().__init__()
        self.data = data
        self.requestName = requestName

        if self.requestName == 'login':
            pass
        elif self.requestName == 'retrieve_friends':
            pass
        elif self.requestName =='retrieve_chat':
            pass
        elif self.requestName =='send_message':
            pass
        elif self.requestName =='new_user':
            pass
        elif self.requestName =='namesLike':
            pass
        elif self.requestName =='addFriend':
            self.userSender = None
            self.userRecip = None

    def toJson(self):
        dictJson = {}
        dictJson['request'] = self.requestName
        dictJson['exception'] = self.exception
        dictJson['data'] = self.data.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        #DEPRECATED
        self.requestName = dictObj['request']
        self.exception = dictObj['exception']

        if self.requestName == 'login':
            self.data = Models.Login().fromJson(dictObj)
        elif self.requestName == 'retrieve_friends':
            self.data = Models.user().fromJson(dictObj)
        elif self.requestName =='retrieve_chat':
            pass
        elif self.requestName =='send_message':
            pass
        elif self.requestName =='new_user':
            pass
        elif self.requestName =='namesLike':
            pass
        elif self.requestName =='addFriend':
            pass

class AddFriendRequest(Request):
    def __init__(self, requestName):
        super().__init__(requestName)
        self.userSender = None
        self.userRecip = None

