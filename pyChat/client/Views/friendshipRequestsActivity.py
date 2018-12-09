from pyChat.client.Views.UIElements.Frames import friendshipRequestsLayout
from pyChat.Models import Models
#from pyChat.client.Controller.ViewController import MainViewController

class friendshipRequestsActivity(friendshipRequestsLayout):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.lstRequests = Models.LstUsers()
        self.controller.retrieveFriendshipRequests()

        self.blockButton.config(command = lambda :self.blockUser())
        self.aceptButton.config(command=lambda: self.aceptUser())
        self.contatos_treeview.bind('<<TreeviewSelect>>', lambda event: self.bindTreeview())

    def fillFriendshipRequests(self, lstRequests: Models.LstUsers):
        self.lstRequests = lstRequests
        self.contatos_treeview.insert_lst_treeView(self.lstRequests.toTreeview())
        self.controller.requestRetrieveFriends()

    def blockUser(self):
        friendship = Models.Friendship()
        friendship.recipUser = self.currentContact
        friendship.accepted = 0
        friendship.blocked = 1
        self.controller.requestBlockUser(friendship)
        self.controller.retrieveFriendshipRequests()

    def aceptUser(self):
        self.controller.requestFriendshipAcepted(self.currentContact)
        self.controller.requestRetrieveFriends()
        self.controller.retrieveFriendshipRequests()


    def bindTreeview(self):
        # Caso haja seleção de contato na lista, a id do contato selecionado é capturada:
        self.idUserSelected = self.contatos_treeview.idd_selection_treeView()
        self.currentContact = self.lstRequests.searchId(self.idUserSelected)
        #self.blockButton.config(state = 'enabled')
        self.aceptButton.config(state = 'enabled')