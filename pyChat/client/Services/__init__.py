import json
from tkinter import messagebox
#from pyChat.client.pyChatApp import sessao
from pyChat.client.Models import Models
from . import Responses, DTP

class ClientHandler:
    def __init__(self, session):
        self.session = session

        self.response = DTP.DataTransfer()

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


    def exceptionHandler(self, Expt = Exception) -> Exception or None:
        self.session.reportException(Expt)