from pyChat.Models import Models
import tkinter
from tkinter import ttk



from pyChat.Models import Models


#class friendshipRequestActivity(friendshipRequestLayot):
class friendshipRequestActivity(tkinter.Toplevel):
    def __init__(self, controller, friendship:Models.Friendship):
        super().__init__()
        self.controller = controller
        self.friendship = friendship
        self.senderUser = friendship.senderUser

        self.instru1 = ttk.Label(self,
                                 text='O usuário '+self.senderUser.userName+
                                      '\n de E-mail: '+self.senderUser.userEmail+
                                      '\ndeseja te adicionar à lista de contatos.')

        self.instru1.grid(row=0, column=0, columnspan = 3,padx = 15, pady=20)

        self.acept = ttk.Button(self, text = 'Aceitar', command = lambda : self.accepted())
        self.acept.grid(row=1, column =0)

        self.acept = ttk.Button(self, text = 'Recusar', command = lambda : self.refused())
        self.acept.grid(row=1, column =1)

        self.acept = ttk.Button(self, text = 'Responder depois', command = lambda : self.destroy())
        self.acept.grid(row=1, column =2)

        self.acept = ttk.Button(self, text = 'Bloquear usuário', command = lambda : self.blocked())
        self.acept.grid(row=1, column =3)


    def accepted(self):
        self.friendship.accepted = 1
        self.controller.requestFriendshipAcepted(self.friendship)
        self.destroy()

    def refused(self):
        self.friendship.accepted = 0
        self.controller.requestFriendshipRefused(self.friendship)
        self.destroy()

    def blocked(self):
        self.friendship.accepted = 0
        self.friendship.blocked = 1
        self.controller.requestUserBlock(self.friendship)
        self.destroy()