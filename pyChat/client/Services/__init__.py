import json
from tkinter import messagebox
#from pyChat.client.pyChatApp import Session
from pyChat.client.Models import Models
from . import Responses, Requests, DTP
from pyChat.client.cliente_tcp import ClientTCP

class ClientRequestManager:
    def __init__(self, session):
        self.session = session
        #self.response = DTP.DataTransfer()
        #self.request = DTP.DataTransfer()

        self.con = ClientTCP.cliente_tcp(self)
        self.con.conecta()

    def sendRequest(self, request):
        self.con.sendRequest(request)

    def handle(self, data):
        # A REQUISIÇÃO É CARREGADA EM UM dict
        dictJson = json.loads(data.decode())
        # E O dict É ENVIADO À CLASSE RESPONSÁVEL POR INSTANCIAR A REQUEST (BUILDER PATTERN)
        response = DTP.DataTransferEval(dictJson).eval()

        if isinstance(response, DTP.InternalExceptions):
            self.exceptionHandler(Exception(response.errorName))

        else:
            if isinstance(response, Responses.ResponseLogin):
                self.session.login(response.user)

            elif isinstance(response, Responses.ResponseRetrieveFriends):
                self.session.setContatos(response.lstUsers)

            elif isinstance(response, Responses.ResponseSendMessage):
                self.session.receiveMessage(response.message)

            elif isinstance(response, Responses.ResponseRetrieveChat):
                self.session.retrieveChat(response.lstMessages)

            elif isinstance(response, Responses.ResponseNamesLike):
                self.session.namesLike(response.namesLike)

            elif isinstance(response, Responses.ResponseNewUser):
                self.session.newUserOK(response.user)

            elif isinstance(response, Responses.ResponseAddFriend):
                self.session.addFriend(response.recipUser)

            else:
                self.session.reportException(Exception('Requisiçao não recuperada!'))


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

    def requestSendMessage(self, message: Models.Message):
        request = Requests.RequestSendMessage(message)
        self.sendRequest(request.toJson())

    def requestNamesLike(self, currentUser:Models.user, namesLike:str):
        request = Requests.RequestNamesLike(currentUser, namesLike)
        self.sendRequest(request.toJson())

    def requestAddFriend(self, currentUser:Models.user, friendEmail:str):
        request = Requests.RequestAddFriend(currentUser, friendEmail)
        self.sendRequest(request.toJson())

    def exceptionHandler(self, Expt = Exception) -> Exception or None:
        self.session.reportException(Expt)