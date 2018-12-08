from pyChat.Models import Models
from pyChat.client.Views.UIElements.Frames import login_ui


class loginActivity(login_ui):
    
    def __init__(self, frame_pai, controller):
        
        super().__init__(frame_pai)
        
        self.controller = controller

        
        self.tit1.config(text = "Bem Vindo ao pyChat!")
        #~ self.tit2.config(text = "Entre com seu login ou crie um usuário...")

        #Abaixo é definido o título da entrada 1
        self.entr1.config_Label(text = 'Usuário (Email):')
        
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
        login = Models.Login()
        login.userEmail = self.entr1.retorna_entr()
        login.password = self.entr2.retorna_entr()
        self.controller.requestLogin(login)

    def __comando_B2__(self):
        self.grid_forget()
        self.controller.newUserActivity()

    def __comando_B3__(self):
        self.controller.helpActivity()
