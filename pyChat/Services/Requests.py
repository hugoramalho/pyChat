from pyChat.Models import Models
from . import DTP


class DataTransferEval:
    def __init__(self, dictJson: dict):
        self.dictJson = dictJson

    def eval(self) -> DTP.DataTransfer:
        objectData = eval(self.dictJson['requestName'])()
        objectData.fromJson(self.dictJson)
        return objectData

class RequestLogin(DTP.DataTransfer):
    def __init__(self, login: Models.Login = Models.Login()):
        super().__init__()
        self.user = login

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.Login().fromJson(dictObj['user'])
        return self


class RequestRetrieveChat(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship = Models.Friendship()):
        super().__init__()
        self.friendship = friendship
        self.senderUser = friendship.senderUser
        self.recipUser = friendship.recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.friendship = Models.Friendship().fromJson(dictObj['friendship'])
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        return self


class RequestRetrieveFriends(DTP.DataTransfer):
    def __init__(self, user: Models.user = Models.user()):
        super().__init__()
        self.user = user

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class RequestSendMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message = Models.Message()):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj['message'])
        return self


class RequestStatusMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message = Models.Message()):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj)
        return self


class RequestNewUser(DTP.DataTransfer):
    def __init__(self, user: Models.user = Models.user()):
        super().__init__()
        self.user = user
    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class RequestAddFriend(DTP.DataTransfer):
    def __init__(self, currentUser: Models.user = Models.user(), friendEmail:str = ''):
        super().__init__()
        self.friendEmail = friendEmail
        self.user = currentUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendEmail'] = self.friendEmail
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict)-> object:
        super().fromJson(dictObj)
        self.friendEmail = dictObj['friendEmail']
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class RequestFriendshipAcepted(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship = Models.Friendship()):
        super().__init__()
        self.friendship = friendship

    def toJson(self):
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.friendship = Models.Friendship().fromJson(dictObj)
        return self


class RequestNamesLike(DTP.DataTransfer):
    def __init__(self, currentUser: Models.user = Models.user(), nameLike:str = ''):
        super().__init__()
        self.namesLike = nameLike
        self.user = currentUser

    def toJson(self):
        dictJson = super().toJson()
        dictJson['namesLike'] = self.namesLike
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict or list):
        super().fromJson(dictObj)
        self.namesLike = dictObj['namesLike']
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class RequestDeleteChat(DTP.DataTransfer):
    def __init__(self, senderUser: Models.user = Models.user(), recipUser: Models.user = Models.user()):
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.lstMessages = Models.LstMessages().fromJson(dictObj['recipUser'])
        return self


class RequestDeleteMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message = Models.Message()):
        super().__init__()
        self.message = message
        self.info = ''

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.info = dictObj['info']
        return self


class RequestBlockUser(DTP.DataTransfer):
    def __init__(self, senderUser: Models.user = Models.user(), recipUser: Models.user = Models.user()):
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        return self


class RequestUnblockUser(DTP.DataTransfer):
    def __init__(self, senderUser: Models.user = Models.user(), recipUser: Models.user = Models.user()):
        super().__init__()
        self.senderUser = senderUser
        self.recipUser = recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.recipUser = Models.user().fromJson(dictObj['recipUser'])
        self.senderUser = Models.user().fromJson(dictObj['senderUser'])
        return self