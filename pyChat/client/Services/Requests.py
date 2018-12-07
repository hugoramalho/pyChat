from . import DTP
from pyChat.client.Models import Models


class RequestLogin(DTP.DataTransfer):
    def __init__(self, login:Models.Login):
        super().__init__()
        self.login = login
        self.user = Models.user()

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.user = Models.user().fromJson(dictObj['user'])
        return self


class RequestRetrieveChat(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship = Models.Friendship()):
        super().__init__()
        self.friendship = friendship
        self.senderUser = friendship.senderUser
        self.recipUser = friendship.recipUser
        self.lstMessages = Models.LstMessages()

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendship'] = self.friendship.toJson()
        dictJson['senderUser'] = self.senderUser.toJson()
        dictJson['recipUser'] = self.recipUser.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.lstMessages = Models.LstMessages().fromJson(dictObj['recipUser'])
        return self


class RequestRetrieveFriends(DTP.DataTransfer):
    def __init__(self, user:Models.user):
        super().__init__()
        self.user = user
        self.lstUsers = Models.LstUsers()

    def toJson(self):
        dictJson = super().toJson()
        dictJson['user'] = self.user.toJson()
        return dictJson

    def fromJson(self, dictObj: dict):
        super().fromJson(dictObj)
        self.lstUsers = Models.LstUsers().fromJson(dictObj['LstFriends'])
        return self


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
        return self


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
        return self


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
        return self


class RequestAddFriend(DTP.DataTransfer):
    def __init__(self, friendEmail:str = ''):
        super().__init__()
        self.friendEmail = friendEmail

    def toJson(self) -> dict:
        dictJson = super().toJson()
        dictJson['friendEmail'] = self.friendEmail
        return dictJson

    def fromJson(self, dictObj: dict)-> object:
        super().fromJson(dictObj)
        self.friendEmail = dictObj['friendEmail']
        return self


class RequestFriendshipAcepted(DTP.DataTransfer):
    def __init__(self, friendship: Models.Friendship):
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
    def __init__(self,nameLike:str):
        super().__init__()
        self.namesLike = nameLike

    def toJson(self):
        dictJson = super().toJson()
        dictJson['namesLike'] = self.namesLike
        return dictJson

    def fromJson(self, dictObj: dict or list):
        super().fromJson(dictObj)
        self.namesLike = Models.LstUsers().fromJson(dictObj)
        return self


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
        return self


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
        return self


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
        return self


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
        return self