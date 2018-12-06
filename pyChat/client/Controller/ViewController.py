from tkinter import Tk, messagebox

from pyChat.client.pyChatApp import sessao
from pyChat.client.Views import chatActivity, addFriendActivity, helpActivity, loginActivity, newUserActivity
from pyChat.client.Models import Models

class MainViewController(Tk):
    def __init__(self, session:sessao):
        super().__init__()
        self.title("pyChat")
        self.resizable(0, 0)

        self.session = session
        self.activityFrames = {}

    @property
    def currentUser(self):
        return self.session.currentUser

    def loginActivity(self):
        self.destroyChildrenFrames()
        frame = loginActivity.login_frame(self, self)
        frame.grid(row=0, column=0, sticky="nsew", ipadx=14, padx=25, pady=25)
        frame.tkraise()
        self.activityFrames['login_frame'] = frame

    def newUserActivity(self):
        self.destroyChildrenFrames()
        frame = newUserActivity.novo_user_frame(self, self)
        frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
        self.activityFrames['novo_user_frame'] = frame
        frame.tkraise()

    def chatActivity(self):
        self.destroyChildrenFrames()
        frame = chatActivity.chat_frame(self, self)
        frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
        self.activityFrames['chat_frame'] = frame
        frame.tkraise()

    def aboutActivity(self):
        #frame = aboutAtivity.something
        # frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
        #self.activityFrames['sobre_frame'] = frame
        pass

    def helpActivity(self):
        frame = helpActivity.helpActivity()
        # frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
        self.activityFrames['ajuda_frame'] = frame
        frame.tkraise()

    def addFriendActivity(self):
        frame = addFriendActivity.addFrame_ui(self)
        # frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
        self.activityFrames['addFriend_frame'] = frame
        # frame.tkraise()

    def login(self, user: Models.user):
        self.chatActivity()

    def setContatos(self, lstFriendsUser: Models.LstUsers):
        self.activityFrames['chat_frame'].setContatos(lstFriendsUser)

    def receiveMessage(self, message: Models.Message):
        self.activityFrames['chat_frame'].append_msg(message)

    def retrieveChat(self, lstMessages:Models.LstMessages):
        self.activityFrames['chat_frame'].carrega_msg(lstMessages)

    def namesLike(self, lstUsers:Models.LstUsers):
        self.activityFrames['chat_frame'].fill_search_contacts_like(lstUsers)

    def addFriend(self, friend:Models.user):
        self.activityFrames['chat_frame'].addFriendList(friend)



    def requestLogin(self, login: Models.Login):
        dictRequest=login.toJson()
        dictRequest['request'] = 'login'
        self.session.sendRequest(dictRequest)


    def requestNewUser(self, user: Models.user):
        dictRequest = user.toJson()
        dictRequest['request'] = 'new_user'
        self.session.sendRequest(dictRequest)


    def requestRetrieveChat(self, userFriend: Models.user):
        friendId = userFriend.idd
        userId = self.session.currentUser.idd
        dictRequest = {'request': 'retrieve_chat', 'userId': userId, 'friendId': friendId}
        # Envia a requisição:
        self.session.sendRequest(dictRequest)


    def requestRetrieveFriends(self):
        dictRequest = self.session.currentUser.toJson()
        dictRequest['request'] = 'retrieve_friends'
        # Envia e recebe feedback do servidor:
        self.session.sendRequest(dictRequest)

    def requestSendMessage(self, message: Models.Message):
        dictRequest = message.toJson()
        dictRequest['request']= 'send_message'
        # Envia e recebe feedback do servidor:
        self.session.sendRequest(dictRequest)


    def requestNamesLike(self, namesLike):
        dic_req = {'request': 'namesLike', 'namesLike': namesLike, 'user': self.session.currentUser.toJson()}
        self.session.sendRequest(dic_req)

    def requestAddFriend(self, friendEmail:str):
        dictRequest = {'friendEmail': friendEmail, 'user': self.session.currentUser.toJson(), 'request': 'addFriend'}
        self.session.sendRequest(dictRequest)

    def destroyChildrenFrames(self):
        if self.winfo_children():
            # O método abaixo retorna uma lista com os activityFrames-filhos do frame atual:
            lstFramesChildren = self.winfo_children()
            # O loop abaixo percorre a lista e os destrói:
            for elemFrame in lstFramesChildren:
                elemFrame.destroy()
        else:
            return None

    def showErrorMessage(self, exceptionTitle: str, exception: str):
        messagebox.showerror('Erro!', exception)

    def showWarningMessage(self, warningTitle:str, warning:str):
        messagebox.showwarning('Atenção!', warning)

    def showInfoMessage(self, infoTitle:str, info:str):
        messagebox.showwarning('Atenção!', info)
