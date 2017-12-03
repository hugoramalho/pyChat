#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  myWhats_app.py
#
#  Ramalho <Ramalho@DESKTOP-MEI8G7T>
#
from pacotes_app.login_frame import *
from pacotes_app.novo_user_frame import *
from pacotes_app.novo_user_frame import *
from pacotes_app.chat_frame import *
from pacotes_app.classes_mywhats import *
from cliente_tcp.cliente_tcp import *
from tkinter import Tk


__author__ = "Ramalho, Hugo"
__copyright__ = "Copyright 2007, Trabalho de Redes -  myWhats_app.py"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Professor Gilmar Vassoler"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"


class sessao(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.con = cliente_tcp()
        self.title("myWhatsApp")
        self.resizable(0, 0)

        self.nome_user = ''
        self.id_user = ''

        # ~ self.title_font = Tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.show_frame("login_frame")

    def show_frame(self, page_name):
        '''Constrói o frame cujo nome foi dado'''
        self.destroi_frames_filhos()

        if page_name == 'login_frame':
            frame = login_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()
        elif page_name == 'novo_user_frame':
            frame = novo_user_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()
        elif page_name == 'chat_frame':

            frame = chat_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

    def destroi_frames_filhos(self):
        if self.winfo_children() != []:
            # O método abaixo retorna uma lista com os frames-filhos do frame atual:
            lst_frames = self.winfo_children()
            # O loop abaixo percorre a lista e os destrói:
            for elem_frame in lst_frames:
                elem_frame.destroy()
        else:
            return None

    def login(self, **kwargs):
        dic_login = {}
        dic_login['req'] = 'login'
        dic_login['nome'] = kwargs.get('usuario')
        dic_login['senha'] = kwargs.get('senha')
        # Envia e recebe feedback do servidor:
        dic_feedback = self.con.envia_req(dic_login)
        return (dic_feedback)

    def novo_user(self, **kwargs):
        dic_user = {}
        dic_user['req'] = 'insere_user'
        dic_user['nome'] = kwargs.get('usuario')
        dic_user['senha'] = kwargs.get('senha')
        # Envia e recebe feedback do servidor:
        dic_feedback = self.con.envia_req(dic_user)
        return (dic_feedback)

    def carrega_conversa(self, **kwargs):
        id_contato = kwargs.get('id_contato')
        id_user = kwargs.get('id_user')

        dic_com = {}
        dic_com['req'] = 'carrega_conversa'
        dic_com['id_contato'] = id_contato
        dic_com['id_user'] = id_user

        # Envia e recebe feedback do servidor:
        dic_com = self.con.envia_req(dic_com)

        lst_conv = dic_com['lst_conv']
        return (lst_conv)

    def carrega_contatos(self):
        dic_contatos = {}
        dic_contatos['req'] = 'carrega_contatos'
        dic_contatos['id_user'] = self.id_user
        # Envia e recebe feedback do servidor:
        dic_contatos = self.con.envia_req(dic_contatos)
        dic_contatos['lst_contatos'] = lst_contatos(**dic_contatos)
        return (dic_contatos)

    def envia_msg(self, **dic_conv):
        dic_conv['req'] = 'envio_msg'
        # Envia e recebe feedback do servidor:
        feedback = self.con.envia_req(dic_conv)
        return (feedback)

    def busca_contato(self, nome_like):
        dic_req = {}
        dic_req['req'] = 'busca_contato'
        dic_req['nome_like'] = nome_like
        # Envia e recebe feedback do servidor:
        dic_req = self.con.envia_req(dic_req)

        # ~ print(dic_req)
        if (dic_req['feedback'] == 0):
            return (dic_req)
        else:
            return ([])


class myWhats_app:
    """
        SUPER CLASSE DO PROGRAMA.
        Unidade funcional do programa encapsulada numa classe.
    """
    def __init__(self):

        self.sessao_atv = sessao()
        self.sessao_atv.mainloop()



def main():

    
    app = myWhats_app()
    

if __name__ == '__main__':
    import sys
    sys.exit(main())




