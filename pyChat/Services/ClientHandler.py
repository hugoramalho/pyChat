import json

# from pyChat.ClientSide.pyChatApp import Session
from pyChat.Models import Models
from pyChat.ClientSide.ClientTCP import ClientTCP
from . import Responses, Requests, DTP


class ClientRequestManager:
    def __init__(self, session):
        self.session = session
        #self.response = DTP.DataTransfer()
        #self.request = DTP.DataTransfer()

        self.con = ClientTCP.cliente_tcp(self)
        self.con.conecta()

    def finishConection(self):
        self.con

    def solveResponse(self, data:bytes) -> Exception or DTP.InternalExceptions or DTP.DataTransfer:
        try:
            # A REQUISIÇÃO É CARREGADA EM UM dict
            dictJson = json.loads(data.decode())
            print('Handle cliente ' + str(dictJson))
            # E O dict É ENVIADO À CLASSE RESPONSÁVEL POR INSTANCIAR A REQUEST (BUILDER PATTERN)
            response = Responses.DataTransferEval(dictJson).eval()
            return response
        except Exception as Expt:
            return Expt

    def sendRequest(self, request):
        self.con.sendRequest(request)

    def handle(self, data):
        response = self.solveResponse(data)
        if isinstance(response, Responses.InternalExceptions or Exception):
            self.exceptionHandler(Exception(response.errorName))
        elif isinstance(response, Exception):
            self.exceptionHandler(response)

        else:
            if isinstance(response, Responses.ResponseLogin):
                self.session.login(response.user)

            elif isinstance(response, Responses.ResponseRetrieveFriends):
                self.session.retrievedContacts(response.lstUsers)

            elif isinstance(response, Responses.ResponseSendMessage):
                self.session.incomingMessage(response.message)

            elif isinstance(response, Responses.ResponseRetrieveChat):
                self.session.retrievedChat(response.lstMessages)

            elif isinstance(response, Responses.ResponseNamesLike):
                self.session.retrievedNamesLike(response.namesLike)

            elif isinstance(response, Responses.ResponseNewUser):
                self.session.reportNewUserOK(response.user)

            elif isinstance(response, Responses.ResponseAddFriend):
                self.session.ResponseAddFriend(response.friendship)

            elif isinstance(response, Responses.ResponseFriendshipAcepted):
                self.session.reportFriendshipAcepted(response.friendship)

            elif isinstance(response, Responses.ResponseFriendshipRequests):
                self.session.retrievedFriendshipRequests(response.lstUsers)

            else:
                self.session.reportException(Exception('Requisiçao não recuperada!'))

    def retrieveFriendshipRequests(self, user:Models.user):
        request = Requests.RequestFriendshipRequests(user)
        self.sendRequest(request.toJson())

    def requestLogin(self, login: Models.Login):
        request = Requests.RequestLogin(login)
        self.sendRequest(request.toJson())

    def requestNewUser(self, user: Models.user):
        request = Requests.RequestNewUser(user)
        self.sendRequest(request.toJson())

    def requestRetrieveChat(self, friendship: Models.Friendship):
        request = Requests.RequestRetrieveChat(friendship)
        self.sendRequest(request.toJson())

    def requestRetrieveFriends(self, currentUser: Models.user):
        request = Requests.RequestRetrieveFriends(currentUser)
        self.sendRequest(request.toJson())

    def requestFriendshipAcepted(self, friendship: Models.Friendship):
        request = Requests.RequestFriendshipAcepted(friendship)
        self.sendRequest(request.toJson())

    def requestBlockUser(self, friendship:Models.Friendship):
        request = Requests.RequestBlockUser(friendship)
        self.sendRequest(request.toJson())

    def requestSendMessage(self, message: Models.Message):
        request = Requests.RequestSendMessage(message)
        self.sendRequest(request.toJson())

    def requestNamesLike(self, currentUser: Models.user, namesLike:str):
        request = Requests.RequestNamesLike(currentUser, namesLike)
        self.sendRequest(request.toJson())

    def requestAddFriend(self, currentUser: Models.user, friendEmail:str):
        request = Requests.RequestAddFriend(currentUser, friendEmail)
        self.sendRequest(request.toJson())


    def exceptionHandler(self, Expt = Exception) -> Exception or None:
        self.session.reportException(Expt)