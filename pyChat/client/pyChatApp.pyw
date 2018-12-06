#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  myWhats_app.py
#
#  Ramalho <Ramalho@DESKTOP-MEI8G7T>
#
from tkinter import *
from tkinter import messagebox

from pyChat.client.cliente_tcp.cliente_tcp import *
from pyChat.client import Services
from pyChat.client.Controller import ViewController
from pyChat.client.Models import Models

#from Views import Models




__author__ = "Ramalho, Hugo"
__copyright__ = "Copyright 2017, Trabalho de Redes -  myWhats_app.py"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Professor Gilmar Vassoler"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"


class sessao:
    def __init__(self):
        self.clientHandler = Services.ClientHandler(self)
        self.currentUser = Models.user()

        self.viewController = ViewController.MainViewController(self)
        self.viewController.loginActivity()
        self.con = cliente_tcp(self.clientHandler)
        self.con.conecta()

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

    def retrieveChat(self, lstMessages:Models.LstMessages):
        self.viewController.retrieveChat(lstMessages)

    def namesLike(self, lstUsers:Models.LstUsers):
        self.viewController.namesLike(lstUsers)

    def newUserOK(self, user:Models.user):
        self.viewController.showInfoMessage('Usuário adicionado!', 'Usuário cadastrado com sucesso!')

    def addFriend(self, friend:Models.user):
        if friend.idd == self.currentUser.idd:
            self.viewController.addFriend(friend)
        else:
            self.viewController.addFriend(friend)
            self.viewController.showInfoMessage('Contato adicionado!', 'Contato '+friend.userName+
                                                ' adicionado com sucesso!\nE-mail: '+friend.userEmail)


    def reportException(self, exception: Exception):
        self.viewController.showInfoMessage('Oh Oh', str(exception))

    def conecta(self):
        try:
            self.con.connect()
        except Exception as Expt:
            self.reportException(Expt)

    def sendRequest(self, request:dict):
        self.con.sendRequest(request)



class myWhats_app:
    """
        SUPER CLASSE DO PROGRAMA.
        Unidade funcional do programa encapsulada numa classe.
    """
    def __init__(self):
        self.sessao_atv = sessao()

def main():
    app = myWhats_app()

if __name__ == '__main__':
    import sys
    sys.exit(main())




