
from .gui_frames import chat_frame_ui, ajuda_frame_ui, sobre_frame_ui

from . import classes_mywhats
from datetime import datetime


class chat_frame(chat_frame_ui):
    
    def __init__(self, frame_pai, sessao_atv):
        super().__init__(frame_pai)
        
        self.sessao_atv = sessao_atv

        #LEMBRAR DE CRIAR METODOS QUE CARREGAMOS OS CONTATOS!
        self.lst_contatos = self.sessao_atv.carrega_contatos()['lst_contatos']
        self.lst_conversa_atv = classes_mywhats.lst_mensagem()
        self.id_contato_atv = None
        
        
        
        self.contatos_treeview.insert_lst_treeView(self.lst_contatos.lst_treeview())
  

        
        
        self.config_opcoes1(command = lambda: self.sessao_atv.show_frame('login_frame'))
        self.config_ajuda1(command = lambda: self.__raise_ajuda__())
        self.config_ajuda2(command = lambda: self.__raise_sobre__())
        self.botao_envia.config(command = lambda: self.__envia_msg__())
        self.entr_msg.bind('<KeyRelease-Return>', lambda event: self.__envia_msg__())
        self.contatos_treeview.bind('<<TreeviewSelect>>', lambda event: self.__carrega_contato__())
        
        self.entr_contatos.bind('<KeyRelease>', lambda event: self.__busca_contato__())
        


    def __raise_ajuda__(self):
        ajuda  = ajuda_frame_ui()

    def __raise_sobre__(self):
        sobre = sobre_frame_ui()


    def __carrega_contato__(self):
        # Caso haja seleção de contato na lista, a id do contato selecionado é capturada:
        self.id_contato_atv = self.contatos_treeview.idd_selection_treeView()
        self.nome_contato = self.lst_contatos.busca_id(self.id_contato_atv).nome_contato
        
        self.conversa_treeview.config_tit_treeView('Conversa com: '+nome_contato)
        
        # O botão de enviar mensagens é habilitado:
        self.botao_envia.config(state = 'enabled')
        # A entrada de texto é habilitada e limpada:
        self.entr_msg.config(state = 'normal')
        self.entr_msg.limpa_entr()
        
        # A lista de conversas daquele contato é carregada:
        self.lst_conversa_atv = classes_mywhats.lst_mensagem(*self.sessao_atv.carrega_conversa(id_contato = self.id_contato_atv, id_user = self.sessao_atv.id_user))
        #~ print(self.lst_conversa_atv.lst_treeview())
        # A caixa de mensagens é limpada (caso usuário esteja transitando de conversas)
        self.conversa_treeview.clear_treeView()
        # As lista de conversas do usuário com o contato selecionado são inseridas na caixa de diálogo:
        self.conversa_treeview.insert_lst_treeView(self.lst_conversa_atv.lst_treeview())

    def __busca_contato__(self):
        nome_like = self.entr_contatos.retorna_entr()
        
        
        if(self.sessao_atv.busca_contato(nome_like) != []):
            
            self.lst_contatos = classes_mywhats.lst_contatos(**self.sessao_atv.busca_contato(nome_like))
            self.contatos_treeview.clear_treeView()
            self.contatos_treeview.insert_lst_treeView(self.lst_contatos.lst_treeview())
        else:
            dic_treev = {}
            dic_treev['text'] = 'Usuário não encontrado!'
            self.contatos_treeview.clear_treeView()
            self.contatos_treeview.insert_kwargs_treeView(**dic_treev)
        
    def __envia_msg__(self):
        conteudo = self.entr_msg.retorna_entr()
        if conteudo != '':
            msg = self.__msg__
            self.entr_msg.limpa_entr()
            feedback = self.sessao_atv.envia_msg(**msg.dic_db())

            if feedback['feedback'] == 0:
                self.conversa_treeview.insert_kwargs_treeView(**msg.dic_treeview())

            else:
                erro = feedback['feedback']
                Expt = str(feedback['Exception'])
                info = 'Ocorreu um erro ao enviar a mensagem!\nErro: "'+Expt+'"'
                self.messagebox_info('Oh oh!', info)

    @property
    def __msg__(self):
        present = datetime.now()
        dic_msg = {}
        dic_msg['data_hora'] = str(present)
        dic_msg['dest'] = self.nome_contato
        dic_msg['rem'] = self.sessao_atv.
        dic_msg['conteudo'] = self.entr_msg.retorna_entr()
        dic_msg['id_dest'] = self.id_contato_atv
        dic_msg['id_user'] = self.sessao_atv.id_user
        dic_msg['id_rem'] = self.sessao_atv.id_user
        msg = classes_mywhats.mensagem(**dic_msg)
        return msg
