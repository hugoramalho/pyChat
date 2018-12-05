
from .Widgets import *


__all__ = ['sub_CBox', 'sub_Menu', 'wd_Entry', 'sub_Text', 'sub_Treeview', 'login_ui', 'novo_user_ui', 'novo_user_ui', 'chat_frame_ui', 'c_janelaPrincipal']








class login_ui(Frame):

    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)



        
        #Subtítulos do programa:
        #O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self, anchor = CENTER)#, width = 18)
        self.tit1.grid(row = 0, column=0, sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)
        
        self.separator = ttk.Separator(self, orient = HORIZONTAL)
        self.separator.grid(row = 1, column=0, sticky = 'we', pady = 2, padx = 2)

        #A entrada 1 é instanciada abaixo:
        self.entr1 = wd_Entry(self)
        self.entr1.grid_frame(row = 2,column = 0, sticky = E+W)
        
        #A entrada 2 é instanciada abaixo:
        self.entr2 = wd_Entry(self, show ='*')
        self.entr2.grid_frame(row = 4,column = 0, sticky = E+W)
        
        
        #O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao1 = ttk.Button(self)
        self.botao1.grid(row = 6, column = 0, sticky = W+E, padx = 2, pady=3)
        
        #O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao2 = ttk.Button(self)
        self.botao2.grid(row = 7, column = 0, sticky = W+E, padx = 2, pady=3)
        

        #O  botao3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao3 = ttk.Button(self)
        self.botao3.grid(row = 8, column = 0, sticky = W+E, padx = 2, pady=3)

    
    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)
    
    def config_tit1(self, **kwargs):
        self.tit1.config(**kwargs)
        
    def config_tit2(self, **kwargs):
        self.tit2.config(**kwargs)

    def config_B1(self, **kwargs):
        self.botao1.config(**kwargs)

    def config_B2(self, **kwargs):
        self.botao2.config(**kwargs)

    def config_B3(self, **kwargs):
        self.botao3.config(**kwargs)

    def grid_frame(self):
        self.grid(row = 0, column=0, sticky = N+S, pady = 2, padx = 2)
        
    def ungrid_frame(self):
        self.grid_forget()
        
    def finaliza(self):
        self.destroy()


class novo_user_ui(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        #Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        #~ self.grid(sticky = E+W+S+N, padx = 25)

        #Subtítulos do programa:
        #O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self, anchor = CENTER)#, width = 18)
        self.tit1.grid(row = 0, column=0, sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)
        
        self.separator = ttk.Separator(self, orient = HORIZONTAL)
        self.separator.grid(row = 1, column=0, sticky = 'we', pady = 2, padx = 2)

        #A entrada 1 é instanciada abaixo:
        self.entr1 = wd_Entry(self)
        self.entr1.grid_frame(row = 2,column = 0, sticky = E+W)

        self.entrMail = wd_Entry(self)
        self.entrMail.grid_frame(row = 3,column = 0, sticky = E+W)

        #A entrada 2 é instanciada abaixo:
        self.entr2 = wd_Entry(self, show ="*")
        self.entr2.grid_frame(row = 4,column = 0, sticky = E+W)
        
        #A entrada 2 é instanciada abaixo:
        self.entr3 = wd_Entry(self, show ="*")
        self.entr3.grid_frame(row = 6,column = 0, sticky = E+W)
        
        
        
        #O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao1 = ttk.Button(self)
        self.botao1.grid(row = 7, column = 0, sticky = W+E, padx = 2, pady=3)
        
        #O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao2 = ttk.Button(self)
        self.botao2.grid(row = 8, column = 0, sticky = W+E, padx = 2, pady=3)
        
        
    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)

    def config_tit1(self, **kwargs):
        self.tit1.config(**kwargs)
        

    def config_B1(self, **kwargs):
        self.botao1.config(**kwargs)

    def config_B2(self, **kwargs):
        self.botao2.config(**kwargs)
    
    def config_B3(self, **kwargs):
        self.botao3.config(**kwargs)
 
    def grid_frame(self):
        self.grid(row = 0, column=0, sticky = N+S, pady = 2, padx = 2)
        
    def ungrid_frame(self):
        self.grid_forget()
        
    def finaliza(self):
        self.destroy()


class chat_frame_ui(Frame):
    
    def __init__(self, frame_pai):
        super().__init__(frame_pai)

        
        self.menu_superior = Menu(self)
        frame_pai.config(menu=self.menu_superior)
        # ~ self.menu_superior.grid(row = 0, column = 0, columnspan = 10)
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Opções":
        self.opcoes = Menu(self.menu_superior, tearoff=0)
        self.menu_superior.add_cascade(menu=self.opcoes, label='Opções')
        #Sub-opções dentro da opção "Arquivo":
        self.opcoes.add_command(label="Trocar usuário")
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.opcoes.add_separator()  #Esse comando adciona um layout de separação entre as opções do menu
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        self.ajuda = Menu(self.menu_superior, tearoff=0)
        self.menu_superior.add_cascade(menu=self.ajuda,label='Ajuda')
        #Sub-opções dentro da opção "Ajuda":
        self.ajuda.add_command(label="Tutorial")
        self.ajuda.add_command(label="Sobre")
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.ajuda.add_separator()
        try:
            frame_pai.config(menu=self.menu_superior)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.frame_pai.tk.call(frame_pai, "config", "-menu", self.menu_superior)

        self.frame_contatos = Frame(self)
        self.frame_contatos.grid(row = 0, column=0, sticky = N+S, padx = 10, pady = 10)
        
        self.separator = ttk.Separator(self, orient = HORIZONTAL)
        self.separator.grid(row = 0, column=1, sticky = 'we', pady = 2, padx = 2)
        
        self.frame_chat = Frame(self)
        self.frame_chat.grid(row = 0, column=2, sticky = N+W+E+S, padx = 3, pady = 3)
        

        self.add_contato_button = ttk.Button(self.frame_contatos, text = 'Adicionar contato', state = 'enabled')
        self.add_contato_button.grid(row=0, column = 0, sticky = 'WE', padx=6 )

        self.contatos_treeview = sub_Treeview(self.frame_contatos, num_cols = 1, height = 20, tit = 'Contatos')
        self.contatos_treeview.config_heading('0', text = 'Nomes:')
        self.contatos_treeview.config_column('#0', width = 150)
        self.contatos_treeview.grid_frame(row = 1, column=0, sticky = N+S)

        
        self.entr_contatos = wd_Entry(self.frame_contatos, tit_Entry ='Buscar contato:')
        self.entr_contatos.grid_frame(row=2, column = 0, sticky = W+E)
        

        self.conversa_treeview = sub_Treeview(self.frame_chat, num_cols = 2, height = 20, tit = 'Selecione um contato para conversar.')
        self.conversa_treeview.config_column('#0', width = 200)
        self.conversa_treeview.config_heading("#0", text = 'Enviado por:')
        self.conversa_treeview.config_column('1', width = 500)
        self.conversa_treeview.config_heading('1', text = 'Mensagem:')
        

        self.conversa_treeview.grid_frame(row = 0, column=0, sticky = N+S, columnspan = 2)  

        
        self.entr_msg = wd_Entry(self.frame_chat, tit_Entry ='Digite a mensagem:', width = 80, state_Entry ='disabled')
        self.entr_msg.insert_Entry('Selecione um contato para conversar!')
        self.entr_msg.grid_frame(row=1, column = 0, sticky = W+E)
        
        self.botao_envia = ttk.Button(self.frame_chat, text = 'enviar', state = 'disabled')
        self.botao_envia.grid(row=1, column = 1, sticky = S )
        
    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)
        
    def config_opcoes1(self, **kwargs):
        self.opcoes.entryconfigure(0, **kwargs)
    
    def config_ajuda1(self, **kwargs):
        self.ajuda.entryconfigure(0, **kwargs)
    
    def config_ajuda2(self, **kwargs):
        self.ajuda.entryconfigure(1, **kwargs)


class ajuda_frame_ui(Toplevel):
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


class sobre_frame_ui(Toplevel):
    def __init__(self):
        super().__init__()
        self.titulo = Label(self, text = 'Sobre')
        self.titulo.grid(row = 0, column = 0, sticky = E+W)


        texto = 'Trabalho de Redes'
        self.instru1 = Label(self, text = texto)
        self.instru1.grid(row = 1, column = 0, sticky = W, padx = 15, pady = 5)
        texto = 'Desenvolvido por Hugo Ramalho, 2017/2'
        self.instru2 = Label(self, text=texto)
        self.instru2.grid(row = 2, column=0, sticky=W, padx = 15, pady = 5)
        texto = 'Licença: GPL'
        self.instru3 = Label(self, text=texto)
        self.instru3.grid(row = 3, column=0, sticky= W, padx = 15, pady = 5)
        texto = 'Contato: ramalho.hg@gmail.com\n ' \
                ' -------------------------------------------------------------------------'
        self.instru4 = Label(self, text=texto)
        self.instru4.grid(row = 4, column=0, sticky= W, padx = 15, pady = 5)
        texto = 'INSTITUTO FEDERAL DO ESPÍRITO SANTO, CAMPUS SERRA'
        self.instru5 = Label(self, text=texto)
        self.instru5.grid(row = 5, column=0, sticky= W, padx = 15, pady = 5)

        self.botao1 = ttk.Button(self, text = 'Ok!', command = self.destroy)
        self.botao1.grid(row = 8, pady = 25)


class AddFriendFrame(Toplevel):
    def __init__(self):
        super().__init__(padx= 20,pady=20)
        self.titulo = Label(self, text = 'Adicionar contato')
        self.titulo.grid(row = 0, column = 0, sticky = N+E+W)


        self.instru1 = Label(self, text = 'Digite o E-mail do contato:')
        self.instru1.grid(row = 1, column = 0, sticky = W, padx = 15, pady = 5)

        self.entr_email = ttk.Entry(self)
        self.entr_email.grid(row=2, column=0, sticky = E+W)

        self.add_button =  ttk.Button(self, text = 'Adicionar!')
        self.add_button.grid(row = 3, column=0, sticky = E+W, padx = 15, pady = 5)

        self.cancel_button =  ttk.Button(self, text = 'Cancelar', command = self.destroy)
        self.cancel_button.grid(row = 4, column=0, sticky = E+W, padx = 15, pady = 5)







class c_janelaPrincipal:

    def __init__(self, master):
        # Bloco (1) Configurando frame principal(janela-pai):
        
        self.master = master
        #Comando abaixo configura a resoluação padrão da janela como sendo a resolução do PC em questão:
        #~ self.master.geometry("{}x{}".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        self.master.geometry('400x600')
        
        #Comando abaixo configura a janela para iniciar como "maximizada":
        #Comando abaixo configura o título da janela:
        self.master.title(' ')
        #Comando abaixo printa no terminal a resolução configurada para a máquina em questão:
        #~ print(self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        
        #Abaixo é declarada a janela-pai
        self.scroll_win = ScrolledWindow(self.master)#, relief = GROOVE, padx = 10, pady = 4)

        self.framePai = self.scroll_win.scrollwindow
        
        #
        #Fim do Bloco (1)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (2) Declaração do menu superior da janela-pai:
        self.menuSuperior = Menu(self.master)
        self.master.config(menu=self.menuSuperior)
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Arquivo":
        self.menuArquivo = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuArquivo, label='Arquivo')
        #Sub-opções dentro da opção "Arquivo":
        self.menuArquivo.add_command(label="Carregar",  command ='')
        self.menuArquivo.add_command(label="Novo",  command = self.load_file_txt)	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuArquivo.add_separator()  #Esse comando adciona um layout de separação entre as opções do menu
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Configurações":
        self.menuConfiguracoes = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuConfiguracoes,label='Ferramentas')
        #Sub-opções dentro da opção "Configurações":,
        self.menuConfiguracoes.add_command(label="Configurações")
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuConfiguracoes.add_separator() 
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        self.menuAjuda = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuAjuda,label='Ajuda')
        #Sub-opções dentro da opção "Ajuda":
        self.menuAjuda.add_command(label="Tutorial")	
        self.menuAjuda.add_command(label="Sobre")	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuAjuda.add_separator()
        
        
        
        #Comando que exibe o menu:
        #master.config(menu=self.menuSuperior)
        
        #Fim do bloco (2)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (3) Declarando sub-frames da janela-pai:
        '''A janela-pai está dividida em três sub-frames, lateral esquerdo, central, lateral direito, e um sub-frame de rodapé.
                Na presente classe, cada um dos três sub-frames não admite sub-divisões, sendo containeres.
                Sendo assim, adimitindo o maior grau de divisão de frames na classe, a janela-pai terá a seguinte divisão:
                
                ______________________________janela-pai______________________________
                |(subFrameLateralEsquerdo)|(subFrameCentral)|(subFrameLateralDireito)|
                |							subFrameInferior-rodapé						 |
                        
        '''	
        
        #Bloco (3.1): Abaixo, é declarado o frame lateral esquerdo. O frame está contido no frame-pai:
        self.frame_esquerdo = Frame(self.framePai, padx ="4", pady = "4")
        self.frame_esquerdo.grid(row = 0, column=0, sticky = N+S)
        
        
        
        #Bloco (3.3): Abaixo, é declarado o frame central. O frame está contido no frame-pai:
        self.frame_central = Frame(self.framePai)#, padx ="4", pady = "4")
        self.frame_central.grid(row = 0, column = 1)#, sticky = N+S+W+E)
    
        


        #Bloco (3.4): Abaixo, é declarado o frame lateral direito. O frame está contido no frame-pai:
        self.frame_direito = Frame(self.framePai, padx ="4", pady = "4")
        self.frame_direito.grid(row = 0, column = 2, sticky = N+S)

        #Bloco (3.5): Abaixo, é declarado o frame inferior no rodapé da do frame-pai(note o columnspan = 3):
        self.frame_infe = Frame(self.framePai, padx ="4")
        self.frame_infe.grid(row = 1, column = 0, columnspan = 3, sticky = W+E)

#####################################################################
#############  FIM DA __init__  #####################################
#####################################################################

    def add_wid_frame_esqr(self, wid_frame):
        self.wid_frame_esq = wid_frame(self.frame_esquerdo)
        return(self.wid_frame_esq)

    def add_wid_frame_cent(self, wid_frame):
        self.wid_frame_cent = wid_frame(self.frame_central)
        return(self.wid_frame_cent)

    def add_wid_frame_dire(self, wid_frame):
        self.wid_frame_dire = wid_frame(self.frame_direito)
        return(self.wid_frame_dire)

    def add_wid_frame_infe(self, wid_frame):
        self.wid_frame_infe = wid_frame(self.wid_frame_infe)
        return(self.wid_frame_infe)



    def pointer_frame_esq(self):
        return(self.frame_esquerdo)

    def pointer_frame_cent(self):
        return(self.frame_central)

    def pointer_frame_dire(self):
        return(self.frame_direito)

    def pointer_frame_infe(self):
        return(self.frame_infe)

    def pointer_frame_master(self):
        return(self.master)



    def load_file_txt(self):
        #A rotina abaixo abre o .txt, retornando um string, tratando eventuais erros com o encode:
        def tryOpen(filename):
            try:
                arq = open(filename, 'r', encoding = 'utf-8')
            except (UnicodeDecodeError, UnicodeEncodeError): #Aqui a função trata erros de enconding
                try:
                    print('\n*** Observação: UnicodeDecodeError, tentando encoding = charmap ***')
                    arq = open(filename, 'r', encoding ='charmap')
                except (UnicodeDecodeError, UnicodeEncodeError):
                    try:
                        print('\n*** Observação: UnicodeDecodeError, tentando encoding = CP-1252 ***')
                        arq = open(filename, 'r', encoding ='cp1252')
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        print('\n*** Atenção, não foi possível carregar o texto:',arqtxt,'por erros no encoding ***')
                        arq.close()	
            string = arq.read()
            arq.close()
            return(string)

        filename =  filedialog.askopenfilename()
        print("\n" + filename)
        string = tryOpen(filename)

        #Abaixo, vamos extrair o nome do texto carregador:
        listaux = filename.split('/')
        nomeTxt = listaux[len(listaux)-1]
        
        
        return(string, nomeTxt)



    def destroi_framesFilhos(self, frame):
        if  frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].destroy()
                cont = cont + 1
        else:
            return None


    def ungrid_framesFilhos(self, frame):
        if  frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].grid_forget()
                cont = cont + 1
        else:
            return None


    def ungrid_framesFilhos_cent(self):
        self.ungrid_framesFilhos(self.frame_central)
    
    def destroi_framesFilhos_cent(self):
        self.destroi_framesFilhos(self.frame_central)


    def ungrid_framesFilhos_esqr(self):
        self.ungrid_framesFilhos(self.frame_esquerdo)


    def ungrid_framesFilhos_dire(self):
        self.ungrid_framesFilhos(self.frame_direito)


    def ungrid_framesFilhos_infe(self):
        self.ungrid_framesFilhos(self.frame_infe)

    def lst_framesFilhos_cent(self):
        return(self.frame_central.winfo_children())

    def finaliza(self):
        self.framePai.destroy()