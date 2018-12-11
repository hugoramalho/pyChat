from datetime import datetime

from pyChat.Models import Models
from pyChat.ClientSide.Views.UIElements.Frames import chat_frame_ui


class chat_frame(chat_frame_ui):
    def __init__(self, frame_pai, controller):
        super().__init__(frame_pai)

        self.controller = controller
        self.controller.requestRetrieveFriends()

        # LEMBRAR DE CRIAR METODOS QUE CARREGAMOS OS CONTATOS!
        self.currentChat = Models.LstMessages

        self.currentContactChat = Models.user()
        self.idUserSelected = self.currentContactChat.idd
        self.userFriendsList = Models.LstUsers()

        self.config_opcoes1(command=lambda: self.controller.loginActivity())
        self.config_ajuda1(command=lambda: self.__raise_ajuda__())
        self.config_ajuda2(command=lambda: self.__raise_sobre__())
        self.botao_envia.config(command=lambda: self.__envia_msg__())
        self.entr_msg.bind('<KeyRelease-Return>', lambda event: self.__envia_msg__())
        self.contatos_treeview.bind('<<TreeviewSelect>>', lambda event: self.__retrieve_chat__())

        #TODO MUDAR ESSA CHAMADA ABAIXO
        self.frame_chat.config(text = 'Seja bem vindo(a) '+ self.controller.session.currentUser.userName)


        self.add_contato_button.config(command=lambda: self.__add_contato__())
        self.solicitations_button.config(command=lambda: self.FriendshipSolicitations())

        self.entr_contatos.bind('<KeyRelease>', lambda event: self.__search_contacts__())

    def FriendshipSolicitations(self):
        self.controller.friendshipRequestsActivity()

    def __add_contato__(self):
        self.controller.addFriendActivity()

    def retrievedContacts(self, lstUser: Models.LstUsers):
        print(lstUser)
        self.userFriendsList = lstUser
        self.contatos_treeview.clear_treeView()
        self.contatos_treeview.insert_lst_treeView(self.userFriendsList.toTreeview())

    def updateFriendsList(self):
        self.contatos_treeview.insert_lst_treeView(self.userFriendsList.toTreeview())

    def __raise_ajuda__(self):
        self.controller.helpActivity()

    def __raise_sobre__(self):
        self.controller.aboutActivity()

    def retrievedChat(self, lstMessage: Models.LstMessages):
        self.lst_conversa_atv = lstMessage
        self.conversa_treeview.clear_treeView()
        self.conversa_treeview.insert_lst_treeView(self.lst_conversa_atv.toTreeview())

    def incomingFriend(self, friend: Models.user):
        self.controller.requestRetrieveFriends()

    def __retrieve_chat__(self):
        # Caso haja seleção de contato na lista, a id do contato selecionado é capturada:
        self.idUserSelected = self.contatos_treeview.idd_selection_treeView()
        self.currentContactChat = self.userFriendsList.searchId(self.idUserSelected)
        # A lista de conversas daquele contato é carregada:
        self.controller.requestRetrieveChat(self.currentContactChat)
        self.conversa_treeview.config_tit_treeView('Conversa com: ' + self.currentContactChat.userName)
        # O botão de enviar mensagens é habilitado:
        self.botao_envia.config(state='enabled')
        # A entrada de texto é habilitada e limpada:
        self.entr_msg.config(state='normal')
        self.entr_msg.limpa_entr()

    def retrievedNamesLike(self, lstUsersLike: Models.LstUsers):
        if (lstUsersLike != []):
            self.userFriendsList = lstUsersLike
            self.contatos_treeview.clear_treeView()
            self.contatos_treeview.insert_lst_treeView(self.userFriendsList.toTreeview())
        else:
            dic_treev = {}
            dic_treev['text'] = 'Usuário não encontrado!'
            self.contatos_treeview.clear_treeView()
            self.contatos_treeview.insert_kwargs_treeView(**dic_treev)

    def __search_contacts__(self):
        nameLike = self.entr_contatos.retorna_entr()
        self.controller.requestNamesLike(nameLike)

    def __envia_msg__(self):
        content = self.entr_msg.retorna_entr()
        if content != '':
            message = self.__msg__
            self.entr_msg.limpa_entr()
            self.controller.requestSendMessage(message)
            self.conversa_treeview.insert_kwargs_treeView(**message.toTreeview())

    def incomingMessage(self, message: Models.Message):
        if self.currentContactChat.idd == message.senderUser.idd:
            self.conversa_treeview.insert_kwargs_treeView(**message.toTreeview())
        else:
            pass

    @property
    def __msg__(self):
        message = {'dateTime': datetime.now(), 'recipUser': self.currentContactChat,
                   'content': self.entr_msg.retorna_entr()}
        return message

    @property
    def __msg__(self):
        message = Models.Message()
        message.dateTime = datetime.now()
        message.recipUser = self.currentContactChat
        message.content = self.entr_msg.retorna_entr()
        return message