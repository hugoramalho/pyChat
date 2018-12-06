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
from pyChat.client.Views.chatActivity import *
from pyChat.client.Views.loginActivity import *
from pyChat.client.Views.newUserActivity import *
from pyChat.client.Views.addFriendActivity import *

#from Views import Models




__author__ = "Ramalho, Hugo"
__copyright__ = "Copyright 2007, Trabalho de Redes -  myWhats_app.py"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Professor Gilmar Vassoler"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"


class sessao(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.con = cliente_tcp(self)
        self.conecta()
        self.title("myWhatsApp")
        self.resizable(0, 0)


        self.userAct = Models.user()
        self.userId = self.userAct.idd
        self.userName = self.userAct.userName
        self.userEmail = self.userAct.userEmail


        self.frames = {}
        # ~ self.title_font = Tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.show_frame("login_frame")

    def show_frame(self, page_name):
        '''Constrói o frame cujo nome foi dado'''
        self.destroi_frames_filhos()

        if page_name == 'login_frame':
            frame = login_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()
            self.frames['login_frame']= frame
            
        elif page_name == 'novo_user_frame':
            frame = novo_user_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            self.frames['novo_user_frame']= frame
            frame.tkraise()
            
        elif page_name == 'chat_frame':
            frame = chat_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            self.frames['chat_frame']= frame
            frame.tkraise()

    def raiseFrame(self, page_name):
        if page_name == 'sobre_frame':
            frame = sobre_frame_ui()
            #frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            self.frames['sobre_frame']= frame
            #frame.tkraise()

        elif page_name == 'ajuda_frame':
            frame = ajuda_frame_ui()
            # frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            self.frames['ajuda_frame'] = frame
            frame.tkraise()

        elif page_name == 'addFriend_frame':
            frame = addFrame_ui(self)
            # frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            self.frames['addFriend_frame'] = frame
            # frame.tkraise()

    def destroi_frames_filhos(self):
        if self.winfo_children() != []:
            # O método abaixo retorna uma lista com os frames-filhos do frame atual:
            lst_frames = self.winfo_children()
            # O loop abaixo percorre a lista e os destrói:
            for elem_frame in lst_frames:
                elem_frame.destroy()
        else:
            return None

    def conecta(self):
        try:
            self.con.conecta()
        except Exception as Expt:
            return Expt


    def handle(self, data):
        print('Client handler. . .')
        request = json.loads(data.decode())
        print(request)

        requestName = request['request']

        if requestName == 'login':
            if request['exception'] == 0:
                self.userAct = self.userAct.fromJson(request['data'])
                self.frames['login_frame'].login(request)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'retrieve_friends':
            if request['exception'] == 0:
                lstFriendsUser = Models.LstUsers().fromJson(request['data'])
                self.frames['chat_frame'].setContatos(lstFriendsUser)
            else:
                messagebox.showwarning('Erro', request['errorName'])
            
        elif requestName == 'send_message':
            if request['exception'] == 0:
                message = Models.Message().fromJson(request['data'])
                print(message)
                print(self.userAct.idd == message.senderId)
                self.frames['chat_frame'].append_msg(message)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'retrieve_chat':
            if request['exception'] == 0:
                lstMessages = Models.LstMessages().fromJson(request['data'])
                self.frames['chat_frame'].carrega_msg(lstMessages)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'namesLike':
            if request['exception'] == 0:
                lstUsers = Models.LstUsers().fromJson(request['data'])
                self.frames['chat_frame'].fill_search_contacts_like(lstUsers)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'new_user':
            if request['exception'] == 0:
                user = Models.user().fromJson(request['data'])
                self.frames['novo_user_frame'].new_user_ok(user)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'addFriend':
            if request['exception'] == 0:
                friend = Models.user().fromJson(request['data'])
                if friend.idd == self.userAct.idd:
                    self.frames['chat_frame'].addFriendList(friend)
                else:
                    self.frames['addFriend_frame'].addFriendOk(friend)
                    self.frames['chat_frame'].addFriendList(friend)
            else:
                messagebox.showwarning('Erro', request['errorName'])
                self.frames['addFriend_frame'].update()
                self.frames['addFriend_frame'].deiconify()


    def login(self, login: Models.Login):
        dictRequest=login.toJson()
        dictRequest['request'] = 'login'
        self.con.envia_req(dictRequest)


    def new_user(self, user: Models.user):
        dictRequest = user.toJson()
        dictRequest['request'] = 'new_user'
        self.con.envia_req(dictRequest)


    def retrieve_chat(self, userFriend: Models.user):
        friendId = userFriend.idd
        userId = self.userAct.idd

        dictRequest = {'request': 'retrieve_chat', 'userId': userId, 'friendId': friendId}
        # Envia a requisição:
        self.con.envia_req(dictRequest)


    def retrieve_friends(self):
        dictRequest = self.userAct.toJson()
        dictRequest['request'] = 'retrieve_friends'
        # Envia e recebe feedback do servidor:
        self.con.envia_req(dictRequest)

    def send_message(self, message: Models.Message):
        dictRequest = message.toJson()
        dictRequest['request']= 'send_message'
        # Envia e recebe feedback do servidor:
        self.con.envia_req(dictRequest)

    def envia_msg(self, **dic_conv):
        dic_conv['req'] = 'envio_msg'
        # Envia e recebe feedback do servidor:
        feedback = self.con.envia_req(dic_conv)
        return (feedback)

    def searchNamesLike(self, namesLike):
        dic_req = {'request': 'namesLike', 'namesLike': namesLike, 'user': self.userAct.toJson()}
        self.con.envia_req(dic_req)

    def addFriend(self, friendEmail:str):
        dictRequest = {'friendEmail': friendEmail, 'user': self.userAct.toJson(), 'request': 'addFriend'}
        self.con.envia_req(dictRequest)



class myWhats_app:
    """
        SUPER CLASSE DO PROGRAMA.
        Unidade funcional do programa encapsulada numa classe.
    """
    def __init__(self):
        self.sessao_atv = sessao()
        self.sessao_atv.mainloop()

def main():
    app = myWhats_app()

if __name__ == '__main__':
    import sys
    sys.exit(main())




