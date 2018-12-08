from tkinter import Tk, messagebox

from pyChat.Models import Models
from pyChat.client.Views import chatActivity, addFriendActivity, helpActivity, loginActivity, newUserActivity, \
    friendshipRequestActivity
from pyChat.client.pyChatApp import Session


class MainViewController(Tk):
    def __init__(self, session:Session):
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
        frame = loginActivity.loginActivity(self, self)
        frame.grid(row=0, column=0, sticky="nsew", ipadx=14, padx=25, pady=25)
        frame.tkraise()
        self.activityFrames['loginActivity'] = frame

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

    def friendshipRequestReceived(self, friendship: Models.Friendship):
        self.activityFrames['friendshipRequestActivity'] = friendshipRequestActivity.friendshipRequestActivity(self, friendship)


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

    def retrieveChat(self, lstMessages: Models.LstMessages):
        self.activityFrames['chat_frame'].carrega_msg(lstMessages)

    def namesLike(self, lstUsers: Models.LstUsers):
        self.activityFrames['chat_frame'].fill_search_contacts_like(lstUsers)

    def addFriend(self, friend: Models.user):
        self.activityFrames['chat_frame'].addFriendList(friend)

    def requestLogin(self, login: Models.Login):
        self.session.requestLogin(login)

    def requestNewUser(self, user: Models.user):
        self.session.requestNewUser(user)



    def requestBlockUser(self, friendship: Models.Friendship):
        self.session.requestBlockUser(friendship)


    def requestRetrieveChat(self, userFriend: Models.user):
        self.session.requestRetrieveChat(userFriend)

    def requestRetrieveFriends(self):
        self.session.requestRetrieveFriends()

    def requestFriendshipAcepted(self, friendship: Models.Friendship):
            self.session.requestFriendshipAcepted(friendship)

    def requestSendMessage(self, message: Models.Message):
        self.session.requestSendMessage(message)

    def requestNamesLike(self, namesLike):
        self.session.requestNamesLike(namesLike)

    def requestAddFriend(self, friendEmail:str):
        self.session.requestAddFriend(friendEmail)


    def showErrorMessage(self, exceptionTitle: str, exception: str):
        messagebox.showerror('Erro!', exception)

    def showWarningMessage(self, warningTitle:str, warning:str):
        messagebox.showwarning('Atenção!', warning)

    def showInfoMessage(self, infoTitle:str, info:str):
        messagebox.showinfo('Atenção!', info)

    def destroyChildrenFrames(self):
        if self.winfo_children():
            # O método abaixo retorna uma lista com os activityFrames-filhos do frame atual:
            lstFramesChildren = self.winfo_children()
            # O loop abaixo percorre a lista e os destrói:
            for elemFrame in lstFramesChildren:
                elemFrame.destroy()
        else:
            return None