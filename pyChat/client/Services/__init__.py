import json
from tkinter import messagebox
from pyChat.client import myWhats_app
from pyChat.client.Models import Models


class ClientHandler:
    def __init__(self, controller: myWhats_app.sessao):
        self.controller = controller

    def handle(self, data):
        print('Client handler. . .')
        request = json.loads(data.decode())
        print(request)

        requestName = request['request']

        if requestName == 'login':
            if request['exception'] == 0:
                self.controller.userAct = self.controller.userAct.fromJson(request['data'])
                self.controller.frames['login_frame'].login(request)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'retrieve_friends':
            if request['exception'] == 0:
                lstFriendsUser = Models.LstUsers().fromJson(request['data'])
                self.controller.frames['chat_frame'].setContatos(lstFriendsUser)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'send_message':
            if request['exception'] == 0:
                message = Models.Message().fromJson(request['data'])
                print(message)
                print(self.controller.userAct.idd == message.senderId)
                self.controller.frames['chat_frame'].append_msg(message)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'retrieve_chat':
            if request['exception'] == 0:
                lstMessages = Models.LstMessages().fromJson(request['data'])
                self.controller.frames['chat_frame'].carrega_msg(lstMessages)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'namesLike':
            if request['exception'] == 0:
                lstUsers = Models.LstUsers().fromJson(request['data'])
                self.controller.frames['chat_frame'].fill_search_contacts_like(lstUsers)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'new_user':
            if request['exception'] == 0:
                user = Models.user().fromJson(request['data'])
                self.controller.frames['novo_user_frame'].new_user_ok(user)
            else:
                messagebox.showwarning('Erro', request['errorName'])

        elif requestName == 'addFriend':
            if request['exception'] == 0:
                friend = Models.user().fromJson(request['data'])
                if friend.idd == self.controller.userAct.idd:
                    self.controller.frames['chat_frame'].addFriendList(friend)
                else:
                    self.controller.frames['addFriend_frame'].addFriendOk(friend)
                    self.controller.frames['chat_frame'].addFriendList(friend)
            else:
                messagebox.showwarning('Erro', request['errorName'])
                self.controller.frames['addFriend_frame'].update()
                self.controller.frames['addFriend_frame'].deiconify()