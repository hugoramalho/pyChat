# -*- coding: utf-8 -*-
#
#  Views
#
#  Ramalho, HUGO <Ramalho@DESKTOP-MEI8G7T>





"""Pacote que guarda as classes funcionais e de interface gráfica"""

__all__ = ['classes_mywhats', 'ajuda_frame', 'chat_frame', 'login_frame', 'novo_user_frame', 'classes_mywhats', 'gui_frames']

"""O módulo classes_mywhats guarda as listas, classes como usuário, mensagem, etc
    O pacote user_interface, guarda os módulos de interface gráfica
    
    O sufixo de cada frame indica a que frame ele se refe, exceto para o módulo gui_frames.
    O módulo gui_frames guarda as "classes abstrats" das interfaces. Apenas especificando 
    quais widgets o frame contém, como eles estão organizados e seus nomes.
    As funções são atribuidas a cada widget são declaradas em outras classes, que herdam suas
    respectivas classes abstratas. Isso torna o código menos carregado.
    
    
    """

import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Handling WM_DELETE_WINDOW protocol")
        self.geometry("500x300+500+200")
        self.make_topmost()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.destroy()

    def center(self):
        """Centers this Tk window"""
        self.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))

    def make_topmost(self):
        """Makes this window the topmost window"""
        self.lift()
        self.attributes("-topmost", 1)
        self.attributes("-topmost", 0)


if __name__ == '__main__':
    App().mainloop()
    
