from datetime import datetime

from pyChat.client.Models import Models
from pyChat.client.Views.UIElements.Frames import chat_frame_ui


class chat_frame(chat_frame_ui):
    def __init__(self, frame_pai, sessao_atv):
        super().__init__(frame_pai)

        self.sessao_atv = sessao_atv
        self.sessao_atv.retrieve_friends()

        # LEMBRAR DE CRIAR METODOS QUE CARREGAMOS OS CONTATOS!
        self.currentChat = Models.LstMessages

        self.currentContactChat = Models.user()
        self.idUserSelected = self.currentContactChat.idd
        self.userFriendsList = Models.LstUsers()


        self.config_opcoes1(command=lambda: self.sessao_atv.show_frame('login_frame'))
        self.config_ajuda1(command=lambda: self.__raise_ajuda__())
        self.config_ajuda2(command=lambda: self.__raise_sobre__())
        self.botao_envia.config(command=lambda: self.__envia_msg__())
        self.entr_msg.bind('<KeyRelease-Return>', lambda event: self.__envia_msg__())
        self.contatos_treeview.bind('<<TreeviewSelect>>', lambda event: self.__carrega_contato__())
        self.add_contato_button.config(command=lambda: self.__add_contato__())

        self.entr_contatos.bind('<KeyRelease>', lambda event: self.__search_contacts__())

    def __add_contato__(self):
        self.sessao_atv.raiseFrame('addFriend_frame')

    def setContatos(self, lstUser: Models.LstUsers):
        print(lstUser)
        self.userFriendsList = lstUser
        self.contatos_treeview.clear_treeView()
        self.contatos_treeview.insert_lst_treeView(self.userFriendsList.toTreeview())

    def updateFriendsList(self):
        self.contatos_treeview.insert_lst_treeView(self.userFriendsList.toTreeview())

    def __raise_ajuda__(self):
        self.sessao_atv.raiseFrame('ajuda_frame')

    def __raise_sobre__(self):
        self.sessao_atv.raiseFrame('sobre_frame')

    def carrega_msg(self, lstMessage: Models.LstMessages):
        self.lst_conversa_atv = lstMessage
        self.conversa_treeview.clear_treeView()
        self.conversa_treeview.insert_lst_treeView(self.lst_conversa_atv.toTreeview())

    def addFriendList(self, friend: Models.user):
        self.sessao_atv.retrieve_friends()



    def __carrega_contato__(self):
        # Caso haja seleção de contato na lista, a id do contato selecionado é capturada:
        self.idUserSelected = self.contatos_treeview.idd_selection_treeView()
        self.currentContactChat = self.userFriendsList.searchId(self.idUserSelected)
        self.conversa_treeview.config_tit_treeView('Conversa com: ' + self.currentContactChat.userName)

        # O botão de enviar mensagens é habilitado:
        self.botao_envia.config(state='enabled')
        # A entrada de texto é habilitada e limpada:
        self.entr_msg.config(state='normal')
        self.entr_msg.limpa_entr()

        # A lista de conversas daquele contato é carregada:
        self.sessao_atv.retrieve_chat(self.currentContactChat)


    def fill_search_contacts_like(self, lstUsersLike: Models.LstUsers):
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
        self.sessao_atv.searchNamesLike(nameLike)


    def __envia_msg__(self):
        content = self.entr_msg.retorna_entr()
        if content != '':
            message = self.__msg__
            self.entr_msg.limpa_entr()
            self.sessao_atv.send_message(message)
            self.conversa_treeview.insert_kwargs_treeView(**message.toTreeview())


    def append_msg(self, message: Models.Message):
        if message.recipId == self.sessao_atv.userAct.idd:
            print(' caiu aqui eja')
            self.conversa_treeview.insert_kwargs_treeView(**message.toTreeview())
        else:
            pass


    @property
    def __msg__(self):
        present = datetime.now()
        message = Models.Message()
        message.dateTime = present
        message.sessionUserId = self.sessao_atv.userAct.idd
        message.senderUser = self.sessao_atv.userAct
        message.recipUser = self.currentContactChat
        message.content = self.entr_msg.retorna_entr()
        return message