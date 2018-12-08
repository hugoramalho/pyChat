from pyChat.client.Views.UIElements.Frames import friendshipRequestsLayout
from pyChat.Models import Models
from pyChat.client.Controller.ViewController import MainViewController

class friendshipRequestsActivity(friendshipRequestsLayout):
    def __init__(self, lstRequests: Models.LstUsers, controller: MainViewController):
        super().__init__()
        self.controller = controller
        self.lstRequests = lstRequests


        self.blockButton.config(command = lambda :self.blockUser())
        self.aceptButton.config(command=lambda: self.aceptUser())

        self.contatos_treeview.clear_treeView()
        self.contatos_treeview.insert_lst_treeView(self.lstRequests.toTreeview())

        self.contatos_treeview.bind('<<TreeviewSelect>>', lambda event: self.bindTreeview())

    def blockUser(self):
        friendship = Models.Friendship()
        friendship.recipUser = self.currentContact
        friendship.accepted = 0
        friendship.blocked = 1
        self.controller.requestBlockUser(friendship)

    def aceptUser(self):
        friendship = Models.Friendship()
        friendship.recipUser = self.currentContact
        friendship.accepted = 1
        self.controller.requestFriendshipAcepted(friendship)

    def bindTreeview(self):
        # Caso haja seleção de contato na lista, a id do contato selecionado é capturada:
        self.idUserSelected = self.contatos_treeview.idd_selection_treeView()
        self.currentContact = self.lstRequests.searchId(self.idUserSelected)


        self.blockButton.config(state = 'enabled')
        self.aceptButton.config(state = 'enabled')

