"""DATA TRANSFER PROTOCOLS"""

from pyChat.Models import Models


class DataTransfer:
    def __init__(self):
        self.requestName = self.__class__.__name__

    def toJson(self) -> dict:
        dictJson = {'requestName': self.__class__.__name__}
        return dictJson

    def fromJson(self, dictObj: dict):
        self.requestName = dictObj['requestName']
        return self


class InternalExceptions(DataTransfer):
    def __init__(self, requestName:DataTransfer, exception: Exception or None = None):
        super().__init__()
        self.requestName = self.__class__.__name__
        self.failedRequest = requestName
        self.errorName = str(exception)
        self.exception = 1

    def toJson(self):
        dictJson = super().toJson()
        dictJson['requestName'] = self.requestName
        dictJson['errorName'] = self.errorName
        print(dictJson)
        return dictJson

    def fromJson(self, dictJson):
        super().fromJson(dictJson)
        self.requestName = dictJson['requestName']
        self.errorName = dictJson['errorName']
        return self


class DataTransferEval:
    def __init__(self, dictJson: dict):
        self.dictJson = dictJson

    def eval(self) -> DataTransfer:
        objectData = eval(self.dictJson['requestName'])()
        objectData.fromJson(self.dictJson)
        return objectData