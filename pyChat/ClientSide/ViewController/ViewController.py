from tkinter import Tk, messagebox

from pyChat.Models import Models
from pyChat.ClientSide.Views import chatActivity, addFriendActivity, helpActivity, loginActivity, newUserActivity, \
    friendshipRequestActivity, friendshipRequestsActivity
from pyChat.ClientSide.pyChatApp import Session


class MainViewController(Tk):
    def __init__(self, session:Session):
        super().__init__()
        self.title("pyChat")
        self.resizable(0, 0)

        self.session = session
        self.activityFrames = {}
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        self.session.finishSession()
        self.destroy()

    @property
    def currentUser(self):
        return self.session.currentUser

    #############################################
    # ABAIXO MÉTODOS DE ALTERNANCIA DE ACTIVITIES
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

    def friendshipRequestReceivedActivity(self, friendship: Models.Friendship):
        self.activityFrames['friendshipRequestActivity'] = friendshipRequestActivity.friendshipRequestActivity(self, friendship)

    def friendshipRequestsActivity(self):
        self.activityFrames['friendshipRequestsActivity'] = friendshipRequestsActivity.friendshipRequestsActivity(self)

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

    #############################
    # ABAIXO MÉTODOS DE retrieved
    def retrievedContacts(self, lstFriendsUser: Models.LstUsers):
        self.activityFrames['chat_frame'].retrievedContacts(lstFriendsUser)

    def incomingMessage(self, message: Models.Message):
        self.activityFrames['chat_frame'].incomingMessage(message)

    def retrievedChat(self, lstMessages: Models.LstMessages):
        self.activityFrames['chat_frame'].retrievedChat(lstMessages)

    def retrievedNamesLike(self, lstUsers: Models.LstUsers):
        self.activityFrames['chat_frame'].retrievedNamesLike(lstUsers)

    def incomingFriend(self, friend: Models.user):
        self.activityFrames['chat_frame'].incomingFriend(friend)

    def retrievedFriendshipRequests(self, lstUsers:Models.LstUsers):
        self.activityFrames['friendshipRequestsActivity'].retrievedFriendshipRequests(lstUsers)
    ############################
    # ABAIXO MÉTODOS DE REQUEST:
    def requestLogin(self, login: Models.Login):
        self.session.requestLogin(login)

    def requestNewUser(self, user: Models.user):
        self.session.requestNewUser(user)

    def requestFriendshipRequests(self):
        self.session.requestFriendshipRequests()

    def requestBlockUser(self, friendship: Models.Friendship):
        self.session.requestBlockUser(friendship)

    def requestRetrieveChat(self, userFriend: Models.user):
        self.session.requestRetrieveChat(userFriend)

    def requestRetrieveFriends(self):
        self.session.requestRetrieveFriends()

    def requestFriendshipAcepted(self, user: Models.LstUsers):
        self.session.requestFriendshipAcepted(user)

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


class ChatPresenter:
    def __init__(self, mainController = MainViewController):
        self.mainController = mainController
        self.session = self.mainController.session

    def sendMessage(self, message: Models.Message):
        self.session.requestSendMessage(message)

    def namesLike(self, namesLike):
        self.session.requestNamesLike(namesLike)

    def retrieveChat(self, userFriend: Models.user):
        self.session.requestRetrieveChat(userFriend)


    def retrieveFriends(self):
        self.session.requestRetrieveFriends()


    def friendshipRequests(self):
        pass


    def setContatos(self, lstFriendsUser: Models.LstUsers):
        self.mainController.activityFrames['chat_frame'].retrievedContacts(lstFriendsUser)

    def receiveMessage(self, message: Models.Message):
        self.mainController.activityFrames['chat_frame'].incomingMessage(message)

    def setChat(self, lstMessages: Models.LstMessages):
        self.mainController.activityFrames['chat_frame'].carrega_msg(lstMessages)

    def setNamesLike(self, lstUsers: Models.LstUsers):
        self.mainController.activityFrames['chat_frame'].fill_search_contacts_like(lstUsers)

    def addFriend(self, friend: Models.user):
        self.mainController.activityFrames['chat_frame'].incomingFriend(friend)

