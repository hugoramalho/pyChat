from pyChat.Models import Models
#from .UIElements import *
# from .UIElements import *
import tkinter

from pyChat.Models import Models
# from .UIElements import *
# from .UIElements import *
import tkinter



from pyChat.Models import Models


#class friendshipRequestActivity(friendshipRequestLayot):
class friendshipRequestActivity(tkinter.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.friendship = Models.Friendship()

    def requestFriendship(self, friendship: Models.Friendship):
        self.friendship = friendship