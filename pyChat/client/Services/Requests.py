from . import DTP
from pyChat.client.Models import Models

class RequestLogin(DTP.DataTransfer):
    def __init__(self, login:Models.Login):
        super().__init__()
        self.login = login

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])


class RequestRetrieveChat(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user, recipUser:Models.user):
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


class RequestRetrieveFriends(DTP.DataTransfer):
    def __init__(self, user:Models.user):
        super().__init__()
        self.user = user

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.lstUsers = Models.LstUsers().fromJson(dictObj['LstFriends'])


class RequestSendMessage(DTP.DataTransfer):
    def __init__(self, message:Models.Message):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj)


class RequestStatusMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message):
        super().__init__()
        self.message = message

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['message'] = self.message.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.message = Models.Message().fromJson(dictObj)


class RequestNewUser(DTP.DataTransfer):
    def __init__(self, user:Models.user):
        super().__init__()
        self.user = user
    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])


class RequestAddFriend(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship = Models.Friendship()):
        super().__init__()
        self.friendship = friendship

    @property
    def bloecked(self):
        return self.friendship.blocked

    @property
    def accepted(self):
        return self.friendship.accepted

    @property
    def senderUser(self):
        return self.friendship.senderUser

    @property
    def recipUser(self):
        return self.friendship.recipUser

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.friendship = Models.Friendship().fromJson(dictObj['friendship'])
        return self


class RequestNamesLike(DTP.DataTransfer):
    def __init__(self,nameLike:str):
        super().__init__()
        self.namesLike = nameLike

    def toJson(self):
        dictJson = super().toJson()
        dictJson['namesLike'] = self.namesLike
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.namesLike = Models.LstUsers().fromJson(dictObj)


class RequestDeleteChat(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user, recipUser:Models.user):
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

class RequestDeleteMessage(DTP.DataTransfer):
    def __init__(self, message: Models.Message):
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


class RequestBlockUser(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user, recipUser:Models.user):
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

class RequestUnblockUser(DTP.DataTransfer):
    def __init__(self, senderUser:Models.user, recipUser:Models.user):
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