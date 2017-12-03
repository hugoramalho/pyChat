# -*- coding: utf-8 -*-
#
#  pacotes_app
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
    
