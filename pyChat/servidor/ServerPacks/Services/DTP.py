"""DATA TRANSFER PROTOCOLS"""

from pyChat.servidor.ServerPacks.Models import Models

class InternalExceptions:
    def __init__(self, requestName, exception: Exception or None = None):
        self.requestName = self.__class__.__name__
        self.errorName = str(exception)
        self.exception = 1

    def toJson(self):
        dictJson = {'request': self.requestName, 'errorName': self.errorName, 'exception': self.exception}
        return dictJson


class DataTransfer:
    def __init__(self):
        self.requestName = self.__class__.__name__
        self.exception = 0

    def toJson(self) -> dict:
        dictJson = {'requestName': self.__class__.__name__}
        return self

    def fromJson(self, dictObj: dict):
        pass


class DataTransferEval:
    def __init__(self, dictJson: dict):
        self.dictJson = dictJson

    def eval(self) -> DataTransfer:
        objectData = eval(self.dictJson['requestName'])()
        objectData.fromJson(self.dictJson)
        return objectData