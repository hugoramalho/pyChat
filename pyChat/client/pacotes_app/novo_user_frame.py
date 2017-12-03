from .gui_frames import novo_user_ui


class novo_user_frame(novo_user_ui):
    
    def __init__(self, frame_pai, sessao_atv):
        super().__init__(frame_pai)

        self.sessao_atv = sessao_atv
        
        self.tit1.config(text = "Criando novo usuário")
        #~ self.tit2.config(text = "Entre com seu login ou crie um usuário...")

        #Abaixo é definido o título da entrada 1
        self.entr1.config_Label(text = 'Nome de usuário:')
        
        #Abaixo é definido o título da entrada 2
        self.entr2.config_Label(text = 'Senha:')

        #Abaixo é definido o título da entrada 3
        self.entr3.config_Label(text = 'Repita a senha:')

        #Abaixo, é definido o nome, e o comando do botão 1
        self.botao1.config(text = "Salvar", command = self.__comando_B1__)
        
        #Abaixo, é definido o nome, e o comando do botão 2
        self.botao2.config(text = "Voltar", command = self.__comando_B2__)

        
        self.entr3.bind('<KeyRelease-Return>', lambda event: self.__comando_B1__())


    def __comando_B1__(self):
        usuario = self.entr1.retorna_entr()
        senha = self.entr2.retorna_entr()
        senha2 = self.entr3.retorna_entr()
        
        if senha != senha2:
            self.messagebox_info('Cadastro', 'As senhas não conferem!')
            self.entr2.limpa_entr()
            self.entr3.limpa_entr()

        else:
            dic_user = self.sessao_atv.novo_user(senha = senha, usuario = usuario)
            if dic_user['feedback'] == 0:
                self.entr1.limpa_entr()
                self.entr2.limpa_entr()
                self.entr3.limpa_entr()
                self.messagebox_info('Cadastro', 'Usuário cadastrado com sucesso!')
                
            else:
                if dic_user['Erro'] == 'usuario ja cadastrado':
                    self.entr2.limpa_entr()
                    self.entr3.limpa_entr()
                    self.messagebox_info('Cadastro', 'Usuário já cadastrado!\nDefina outro nome de usuário.')
            

    def __comando_B2__(self):
        self.grid_forget()
        self.sessao_atv.show_frame('login_frame')
        
    




