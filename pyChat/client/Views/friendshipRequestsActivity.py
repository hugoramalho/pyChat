from pyChat.client.Views.UIElements.Frames import friendshipRequestsLayout
from pyChat.Models import Models

class friendshipRequestsActivity(friendshipRequestsLayout):
    def __init__(self, lstRequests: Models.LstUsers, controller):
        super().__init__()
        self.controller = controller
        self.lstRequests = lstRequests

