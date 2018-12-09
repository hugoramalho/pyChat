from tkinter import messagebox

from pyChat.Models import Models
from pyChat.ClientSide.Views.UIElements import Frames


class addFrame_ui(Frames.AddFriendFrame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.add_button.config(command= lambda: self.addFriend())
        self.add_button.bind('<KeyRelease-Return>', lambda event: self.addFriend())

        self.friendEmail =''

    def addFriend(self):
        self.friendEmail = self.entr_email.get()
        if self.friendEmail != '':
            self.controller.requestAddFriend(self.friendEmail)
            self.controller.requestRetrieveFriends()
        else:
            pass

    def addFriendOk(self, user: Models.user):
        self.entr_email.delete(0, 'end')
        messagebox.showinfo('Novo contato','Usuário adicionado com sucesso!\nNome: ' + user.userName + '\nEmail: ' + user.userEmail)
        self.controller.requestRetrieveFriends()
        self.update()
        self.deiconify()


    def addFriendNotOk(self):
        self.entr_email.limpa_entr()
        messagebox.showinfo('Novo contato','Usuário não encontrado!\nEmail: ' + self.friendEmail)
        self.update()
        self.deiconify()