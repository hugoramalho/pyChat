#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  myWhats_app.py
#
#  Ramalho <Ramalho@DESKTOP-MEI8G7T>
#

from pyChat import Services
from pyChat.Models import Models
from pyChat.client.Controller import ViewController

__author__ = "Ramalho, Hugo"
__copyright__ = "Copyright 2017, Trabalho de Redes -  myWhats_app.py"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Professor Gilmar Vassoler"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"


class Session:
    def __init__(self):
        self.clientHandler = Services.ClientRequestManager(self)
        self.currentUser = Models.user()
        self.viewController = ViewController.MainViewController(self)
        self.viewController.loginActivity()
        self.viewController.mainloop()

    def login(self, user: Models.user):
        self.currentUser = user
        self.viewController.chatActivity()

    def setContatos(self, lstFriendsUser: Models.LstUsers):
        self.viewController.setContatos(lstFriendsUser)

    def receiveMessage(self, message: Models.Message):
        if message.senderId == self.currentUser.idd:
            pass
        else:
            self.viewController.receiveMessage(message)

    def friendshipRequest(self, friendship: Models.Friendship):
        if friendship.recipUser.idd == self.currentUser.idd:
            self.viewController.friendshipRequestActv(friendship)

    def retrieveChat(self, lstMessages: Models.LstMessages):
        self.viewController.retrieveChat(lstMessages)

    def namesLike(self, lstUsers: Models.LstUsers):
        self.viewController.namesLike(lstUsers)

    def newUserOK(self, user: Models.user):
        self.viewController.showInfoMessage('Usuário adicionado!', 'Usuário cadastrado com sucesso!')

    def addFriend(self, friend: Models.user):
        if friend.idd == self.currentUser.idd:
            self.viewController.addFriend(friend)
        else:
            self.viewController.addFriend(friend)
            self.viewController.showInfoMessage('Contato adicionado!', 'Contato '+friend.userName+
                                                ' adicionado com sucesso!\nE-mail: '+friend.userEmail)

    def reportException(self, exception: Exception):
        self.viewController.showInfoMessage('Oh Oh', str(exception))

    def requestLogin(self, login: Models.Login):
        self.clientHandler.requestLogin(login)

    def requestNewUser(self, user: Models.user):
        self.clientHandler.requestNewUser(user)

    def requestRetrieveChat(self, friend: Models.user):
        friendship = Models.Friendship(self.currentUser, friend)
        self.clientHandler.requestRetrieveChat(friendship)

    def requestRetrieveFriends(self):
        currentUser = self.currentUser
        self.clientHandler.requestRetrieveFriends(currentUser)

    def requestFriendshipAcepted(self, friendship: Models.Friendship):
        # VERIFICAÇÃO FEITA:
        if friendship.recipUser.idd == self.currentUser.idd and friendship.accepted == 1 and friendship.blocked == 0:
            self.clientHandler.requestFriendshipAcepted(friendship)
        else:
            self.viewController.showErrorMessage('Oh Oh!', 'Erro ao processar a requisição:\n'+str(friendship))

    def requestSendMessage(self, message: Models.Message):
        message.senderUser = self.currentUser
        self.clientHandler.requestSendMessage(message)

    def requestNamesLike(self, namesLike:str):
        currentUser = self.currentUser
        self.clientHandler.requestNamesLike(currentUser, namesLike)

    def requestAddFriend(self, friendEmail:str):
        currentUser = self.currentUser
        self.clientHandler.requestAddFriend(currentUser, friendEmail)


class myWhats_app:
    """
        SUPER CLASSE DO PROGRAMA.
        Unidade funcional do programa encapsulada numa classe.
    """
    def __init__(self):
        self.sessao_atv = Session()

def main():
    app = myWhats_app()

if __name__ == '__main__':
    import sys
    sys.exit(main())




