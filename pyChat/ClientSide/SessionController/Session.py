from pyChat.Models import Models
from pyChat.Services import ClientHandler
from pyChat.ClientSide.ViewController import ViewController


class Session:
    def __init__(self):
        self.clientHandler = ClientHandler.ClientRequestManager(self)
        self.currentUser = Models.user()
        self.viewController = ViewController.MainViewController(self)
        self.viewController.loginActivity()
        self.viewController.mainloop()

    def finishSession(self):
        self.clientHandler.finishConection()

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

    def freindshipRequest(self, friendship: Models.Friendship):
        if friendship.recipUser.idd == self.currentUser.idd:
            self.viewController.friendshipRequestActv(friendship)
        else:
            self.viewController.friendshipRequestFeedbackActv(friendship)

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
    def fillFriendshipRequests(self, lstUsers:Models.LstUsers):
        self.viewController.fillFriendshipRequests(lstUsers)

    def ResponseAddFriend(self, friendship:Models.Friendship):
        recipId = friendship.recipUser.idd
        senderId = friendship.senderUser.idd
        if self.currentUser.idd == recipId:
            self.viewController.friendshipRequestReceived(friendship)
        elif self.currentUser.idd == senderId:
            self.reportFriendshipSent(friendship)

    def reportFriendshipAcepted(self, friendship:Models.Friendship):
        recipName = friendship.recipUser.userName
        recipEmail = friendship.recipUser.userEmail
        if friendship.senderUser.idd != self.currentUser.idd:

            self.viewController.showInfoMessage('Pedido aceito!','O usuário '+recipName+
                                                '\nde E-mail: '+recipEmail+
                                                '\nAceitou seu pedido de amizade!' )
        else:
            self.viewController.showInfoMessage('Usuário aceito!','O usuário '+recipName+
                                                '\nde E-mail: '+recipEmail+
                                                '\nFaz parte da sua lista de contatos!' )



    def reportFriendshipSent(self, friendship:Models.Friendship):
        recipName = friendship.recipUser.userName
        recipEmail = friendship.recipUser.userEmail
        self.viewController.showInfoMessage('Pedido enviado!','O usuário '+recipName+
                                            '\nde E-mail: '+recipEmail+
                                            '\nrecebeu seu pedido de amizade!' )

    def reportException(self, exception: Exception):
        self.viewController.showInfoMessage('Oh Oh', str(exception))

    def requestBlockUser(self, friendShip: Models.Friendship):
        friendShip.senderUser = self.currentUser
        self.clientHandler.requestBlockUser(friendShip)

    def retrieveFriendshipRequests(self):
        self.clientHandler.retrieveFriendshipRequests(self.currentUser)

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

    def requestFriendshipAcepted(self, user: Models.user):
        # VERIFICAÇÃO FEITA:
        friendship = Models.Friendship()
        friendship.recipUser = user
        friendship.accepted = 1
        friendship.blocked = 0
        friendship.senderUser = self.currentUser
        self.clientHandler.requestFriendshipAcepted(friendship)

    def requestSendMessage(self, message: Models.Message):
        message.senderUser = self.currentUser
        self.clientHandler.requestSendMessage(message)

    def requestNamesLike(self, namesLike:str):
        currentUser = self.currentUser
        self.clientHandler.requestNamesLike(currentUser, namesLike)

    def requestAddFriend(self, friendEmail:str):
        currentUser = self.currentUser
        self.clientHandler.requestAddFriend(currentUser, friendEmail)