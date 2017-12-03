
from .gui_frames import login_ui, ajuda_frame_ui



class login_frame(login_ui):
    
    def __init__(self, frame_pai, sessao_atv):
        
        super().__init__(frame_pai)
        
        self.sessao_atv = sessao_atv
        
        self.tit1.config(text = "Bem Vindo ao myWhatsApp!")
        #~ self.tit2.config(text = "Entre com seu login ou crie um usuário...")


        #Abaixo é definido o título da entrada 1
        self.entr1.config_Label(text = 'Usuário:')
        
        #Abaixo é definido o título da entrada 2
        self.entr2.config_Label(text = 'Senha:')
        
        #Abaixo, é definido o nome, e o comando do botão 1
        self.botao1.config(text = "Login", command = self.__comando_B1__)
        
        #Abaixo, é definido o nome, e o comando do botão 2
        self.botao2.config(text = "Novo usuário", command = self.__comando_B2__)
        
        #Abaixo, é definido o nome, e o comando do botão 3
        self.botao3.config(text = "Ajuda", command = self.__comando_B3__)
        
        self.entr2.bind('<KeyRelease-Return>', lambda event: self.__comando_B1__())

        #~ self.grid(sticky = W+E)

    def __comando_B1__(self):
        usuario = self.entr1.retorna_entr()
        senha = self.entr2.retorna_entr()
        #~ print(usuario, senha)
        
        
        dic_login = self.sessao_atv.login(senha = senha, usuario = usuario)
        # Caso o feedback seja igual a zero, o fluxo de eventos se deu da forma correta:
        if dic_login['feedback'] == 0:
            # Entao, o usuario ativo é preenchido:
            #~ self.sessao_atv.user_atv = contato(id_contato = dic_login['id_user'] , nome_contato = )
            self.sessao_atv.id_user = dic_login['id_user']
            self.sessao_atv.nome_user = dic_login['nome_user']
            
            # A tela de login é desfeita:
            self.grid_forget()
            # E a sessão abre a tela de chat:
            self.sessao_atv.show_frame('chat_frame')
        
        # Caso o feedback retorne algo diferente de zero:
        else:
            # As execeções capturadas pelos 'try' são tratadas:
            if dic_login['Erro'] == 'Senha incorreta':
                self.entr2.limpa_entr()
                self.messagebox_info('Login', 'Senha incorreta!')
            
            elif dic_login['Erro'] == 'usuario nao encontrado':
                self.entr2.limpa_entr()
                self.messagebox_info('Login', 'Usuário não encontrado!')
                
            elif dic_login['Erro'] == 'falha na conexão':
                self.entr2.limpa_entr()
                self.messagebox_info('Login', 'Falha na comunicação com o servidor!\nVerifique se o servidor está online')
            


    def __comando_B2__(self):
        self.grid_forget()
        self.sessao_atv.show_frame('novo_user_frame')
        
        

    def __comando_B3__(self):
        # def __raise_ajuda__(self, top_frame):
        ajuda = ajuda_frame_ui()