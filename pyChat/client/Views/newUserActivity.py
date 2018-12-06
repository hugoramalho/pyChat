from pyChat.client.Models import Models
from pyChat.client.Views.UIElements.Frames import novo_user_ui


class novo_user_frame(novo_user_ui):
    def __init__(self, frame_pai, controller):
        super().__init__(frame_pai)

        self.controller = controller

        self.tit1.config(text="Criando novo usuário")
        # ~ self.tit2.config(text = "Entre com seu login ou crie um usuário...")

        # Abaixo é definido o título da entrada 1
        self.entr1.config_Label(text='Nome de usuário:')

        # Abaixo é definido o título da entrada 2
        self.entr2.config_Label(text='Senha:')

        self.entrMail.config_Label(text='Email:')

        # Abaixo é definido o título da entrada 3
        self.entr3.config_Label(text='Repita a senha:')

        # Abaixo, é definido o nome, e o comando do botão 1
        self.botao1.config(text="Salvar", command=self.__comando_B1__)

        # Abaixo, é definido o nome, e o comando do botão 2
        self.botao2.config(text="Voltar", command=self.__comando_B2__)

        self.entr3.bind('<KeyRelease-Return>', lambda event: self.__comando_B1__())

    def __comando_B1__(self):
        user = Models.user()
        user.userName = self.entr1.retorna_entr()
        user.userEmail = self.entrMail.retorna_entr()
        user.password = self.entr2.retorna_entr()
        password2 = self.entr3.retorna_entr()

        if user.password != password2:
            self.messagebox_info('Cadastro', 'As senhas não conferem!')
            self.entr2.limpa_entr()
            self.entr3.limpa_entr()
        else:
            self.controller.requestNewUser(user)

    def newUserOK(self, user: Models.user):
            self.entr1.limpa_entr()
            self.entr2.limpa_entr()
            self.entr3.limpa_entr()
            self.entrMail.limpa_entr()
            self.messagebox_info('Cadastro', 'Usuário cadastrado com sucesso!\nNome: '+user.userName+'\nEmail: '+user.userEmail)

    def __comando_B2__(self):
        self.grid_forget()
        self.controller.loginActivity()