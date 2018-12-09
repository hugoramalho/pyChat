from tkinter import *
from tkinter import ttk

class helpActivity(Toplevel):
    def __init__(self):
        super().__init__()
        self.titulo = Label(self, text = 'Ajuda')
        self.titulo.grid(row = 0, column = 0, sticky = E+W)


        texto = '1) Para login, digite usuário e senha. Ex: usuário: HUGO, senha: 123456'
        self.instru1 = Label(self, text = texto)
        self.instru1.grid(row = 1, column = 0, sticky = W, padx = 15, pady = 5)
        texto = '2) Para cadastrar um novo usuário, defina um nome ainda não cadastrado, e uma senha'
        self.instru2 = Label(self, text=texto)
        self.instru2.grid(row = 2, column=0, sticky=W, padx = 15, pady = 5)
        texto = '3) Para conversar, selecione um contato na lista e clique no seu respectivo nome'
        self.instru3 = Label(self, text=texto)
        self.instru3.grid(row = 3, column=0, sticky= W, padx = 15, pady = 5)
        texto = '4) Para trocar de sessão, acesse o menu superior: Opções -> Trocar Usuário\n ' \
                ' -------------------------------------------------------------------------'
        self.instru4 = Label(self, text=texto)
        self.instru4.grid(row = 4, column=0, sticky= W, padx = 15, pady = 5)
        texto = 'Erros comuns:'
        self.instru5 = Label(self, text=texto)
        self.instru5.grid(row = 5, column=0, sticky= W, padx = 15, pady = 5)
        texto = '1) Falha na comunicação com o servidor: A aplicação servidora não está online'
        self.instru6 = Label(self, text=texto)
        self.instru6.grid(row = 6, column=0, sticky=W, padx = 15, pady = 5)
        texto = '2) Usuário inexistente: Usuário não cadastrado ou teve sua conta excluída'
        self.instru7 = Label(self, text=texto)
        self.instru7.grid(row = 7, column=0, sticky=W, padx = 15, pady = 5)

        self.botao1 = ttk.Button(self, text = 'Ok!', command = self.destroy)
        self.botao1.grid(row = 8, pady = 25)