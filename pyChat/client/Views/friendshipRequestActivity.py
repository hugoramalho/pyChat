from pyChat.client.Models import Models
#from .UIElements import *
import tkinter

#class friendshipRequestActivity(friendshipRequestLayot):
class friendshipRequestActivity(tkinter.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.friendship = Models.Friendship()

    def requestFriendship(self, friendship: Models.Friendship):
        self.friendship = friendship