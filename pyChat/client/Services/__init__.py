import json
from tkinter import messagebox
#from pyChat.client.pyChatApp import sessao
from pyChat.client.Models import Models


class ClientHandler:
    def __init__(self, session):
        self.session = session


    def handle(self, data):
        self.request = json.loads(data.decode())

        catch = self.exceptionHandler()
        if isinstance(catch, Exception):
            self.session.reportException(catch)

        else:
            requestName = self.request['request']

            if requestName == 'login':
                user = Models.user().fromJson(self.request['data'])
                self.session.login(user)

            elif requestName == 'retrieve_friends':
                lstFriendsUser = Models.LstUsers().fromJson(self.request['data'])
                self.session.setContatos(lstFriendsUser)

            elif requestName == 'send_message':
                message = Models.Message().fromJson(self.request['data'])
                self.session.receiveMessage(message)

            elif requestName == 'retrieve_chat':
                lstMessages = Models.LstMessages().fromJson(self.request['data'])
                self.session.retrieveChat(lstMessages)

            elif requestName == 'namesLike':
                lstUsers = Models.LstUsers().fromJson(self.request['data'])
                self.session.namesLike(lstUsers)

            elif requestName == 'new_user':
                user = Models.user().fromJson(self.request['data'])
                self.session.newUserOK(user)

            elif requestName == 'addFriend':
                friend = Models.user().fromJson(self.request['data'])
                self.session.addFriend(friend)

            else:
                self.session.reportException(Exception('Requisiçao não recuperada!'))


    def exceptionHandler(self) -> Exception or None:
        if self.request['exception'] != 0:
            return Exception(self.request['errorName'])
        else:
            return None