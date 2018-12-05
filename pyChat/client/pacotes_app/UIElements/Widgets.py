from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


from tkinter import *
from tkinter import ttk

class wd_Entry(Entry):
    def __init__(self, framePai, **kwargs):
        # Abaixo são ajustados os atributos da Entry:
        self.tit_Entry_text = kwargs.get('tit_Entry', 'Título')
        self.set_Entry_default = kwargs.get('set_Entry_default', 'Opções')
        self.state_Entry = kwargs.get('state_Entry', 'normal')
        self.width_Entry = kwargs.get('width', 20)
        self.show = kwargs.get('show', '')

        self.frameLocal = Frame(framePai)
        self.tit_Entry = Label(self.frameLocal, text=self.tit_Entry_text)
        self.var_Entry = StringVar()

        # Abaixo a Entry é instanciada, por meio de sua classe pai, e recebendo os atributos ajustados
        super().__init__(self.frameLocal, textvariable=self.var_Entry, width=self.width_Entry, state=self.state_Entry,
                         show=self.show)

    def config_Label(self, **kwargs):
        self.tit_Entry.config(kwargs)

    def config_Entry(self, **kwargs):
        self.Entry.config(kwargs)

    def pointer_Entry(self):
        return (self.Entry)

    def pointer_tit_Entry(self):
        return (self.tit_Entry)

    def retorna_entr(self):
        print(self.var_Entry.get())
        return (self.var_Entry.get())

    def insert_Entry(self, txt):
        if self['state'] != 'normal':
            state = self['state']
            self.config(state='normal')
            self.limpa_entr()
            self.delete(0, "end")
            self.insert('end', txt)
            self.config(state=state)
        else:
            self.limpa_entr()
            self.insert('end', txt)

    def destroy_frame(self):
        self.frameLocal.destroy()

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 2)
        padx = kwargs.get('padx', 2)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)
        self.tit_Entry.grid(row=0, column=0, sticky=W, columnspan=columnspan)
        self.grid(row=1, column=0, sticky=sticky, columnspan=columnspan)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def limpa_entr(self):
        self.delete(0, "end")


class sub_Treeview(ttk.Treeview):
    def __init__(self, framePai, **kwargs):
        self.quantCol = kwargs.get('num_cols', 4)
        self.tit = kwargs.get('tit', 'Título')
        self.height = kwargs.get('height', 4)
        self.selectmode = kwargs.get('selectmode', 'browse')

        self.frameLocal = Frame(framePai)

        self.tit_treeView = Label(self.frameLocal, text=self.tit)
        self.tit_treeView.grid(row=0, column=0, sticky=W)

        columnTuple = self.__column_tuple__()
        super().__init__(self.frameLocal, height=self.height, style="Treeview", selectmode='browse',
                         columns=columnTuple)
        self.grid(row=1, column=0)
        self.__column_constr__()

        # Bloco das Scrollbars(barras de rolagem):
        self.scrollbarY = Scrollbar(self.frameLocal, command=self.yview)
        self.scrollbarY.grid(row=1, column=1, sticky=N + S)
        # Bloco  Declaradas a Scrollbar, treeView1 é configurado a recebê-las:
        self.config(yscrollcommand=self.scrollbarY.set)

    def pointer_treeView(self):
        return (self)

    def config_treeView(self, **kwargs):
        self.config(kwargs)

    def config_Label(self, **kwargs):
        self.tit_treeView(self, **kwargs)

    def config_tit_treeView(self, tit):
        self.tit_treeView.config(text=tit)

    def config_tit_col_treeView(self, col, titulo):
        if type(col) != str:
            col = str(col)
        if col == '0':
            col = '#0'
        self.heading(col, text=titulo)

    def selection_treeView(self):
        return (self.selection())

    def idd_selection_treeView(self):
        print(self.selection())
        try:
            print(self.selection()[0])
            return (int(self.selection()[0]))
        except Exception as Expt:
            print(Expt)
            pass

    def item_treeView(self, idd):
        return (self.item(idd))

    def __column_tuple__(self):

        lstAux = []
        if self.quantCol == 1:
            columnTuple = tuple(lstAux)

        else:
            n = 0
            while n < (self.quantCol - 1):
                quant = n + 1
                columnAux = str(quant)
                lstAux.append(columnAux)
                n = n + 1
            columnTuple = tuple(lstAux)
        return (columnTuple)

    def config_heading(self, index, **kwargs):
        if index == 0 or index == '0':
            index = '#0'
        self.heading(index, **kwargs)

    def config_column(self, index, **kwargs):
        if index == 0 or index == '0':
            index = '#0'
        self.column(index, **kwargs)

    def __column_constr__(self):
        self.heading("#0", text="text")
        self.column("#0", width=245, stretch=0)

        n = 1
        while n < (self.quantCol):
            columnAux = str(n)
            self.heading(columnAux, text="coluna 1")
            self.column(columnAux, width=100, stretch=0)
            n = n + 1

    def insert_kwargs_treeView(self, **kwargs):

        idd = kwargs.get('idd', None)
        text = kwargs.get('text', '')
        values = kwargs.get('values', [])

        parent = kwargs.get('parent', '')
        index = kwargs.get('index', 0)

        self.insert('', index, iid=idd, text=text, values=values)

    def insere_elem_treeView(self, value0='', value1='', value2='', value3='', value4='', **kwargs):
        idd = kwargs.get('idd', None)
        elems = (value1, value2, value3, value4)
        self.insert('', 0, iid=idd, text=value0, values=elems)
        # ~ print('Dentro do insere:', *self.treeView.get_children())

    def insere_lst_elem_treeView(self, *lst_args, **kwargs):
        lst_itens = lst_args[0]  # Desempacotando o argumento
        # ~ print('\nTESTE empacotado', lst_itens)
        # ~ print('\nTESTE desempacotado', lst_itens[0])
        idd = kwargs.get('idd', None)  # Adquirindo a id do elemento
        self.insert('', 0, iid=idd, text=lst_itens[0], values=lst_itens[1:])

    def insert_lst_treeView(self, lst):
        for elem_kw in lst:
            self.insert_kwargs_treeView(**elem_kw)

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def clear_treeView(self):
        self.delete(*self.get_children())

    def destroy_frame(self):
        self.destroy()
        self.frameLocal.destroy()


class sub_Text:
    def __init__(self, framePai, **kwargs):
        self.tit = kwargs.get('tit', 'Título')
        self.state = kwargs.get('state', NORMAL)
        self.width = kwargs.get('width', 50)
        self.height = kwargs.get('height', 4)
        self.scrollbarx = kwargs.get('scrollbarx', True)
        self.scrollbary = kwargs.get('scrollbary', True)
        self.bd = kwargs.get('bd', 3)

        # Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frameLocal = Frame(framePai)

        self.tit_text = ttk.Label(self.frameLocal, text=self.tit)
        self.tit_text.grid(row=0, column=0, sticky=W)

        self.blocoText = Text(self.frameLocal, insertborderwidth=5, bd=self.bd, font="Arial 9", wrap=WORD,
                              width=self.width, height=self.height, state=self.state, autoseparators=True)
        self.blocoText.grid(row=1, column=0)

        self.__scrollbar_constr__()


        # ~ self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        # ~ self.separador1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")

    def config_Text(self, **kwargs):
        self.blocoText.config(kwargs)

    def return_text(self):
        text = self.blocoText.get(1.0, "end")
        return (text)

    def config_tit_text(self, text):
        self.tit_text.config(text=text)

    def __scrollbar_constr__(self):
        if self.scrollbarx == True:
            self.scrollbarX = Scrollbar(self.frameLocal, command=self.blocoText.xview, orient=HORIZONTAL)
            self.scrollbarX.grid(row=2, column=0, sticky=E + W)
            self.blocoText.config(xscrollcommand=self.scrollbarX.set)

        if self.scrollbary == True:
            self.scrollbarY = Scrollbar(self.frameLocal, command=self.blocoText.yview, orient=VERTICAL)
            self.scrollbarY.grid(row=1, column=1, sticky=N + S)
            self.blocoText.config(yscrollcommand=self.scrollbarY.set)

    def insert_text(self, txtStr):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete(1.0, END)
        self.blocoText.insert(1.0, txtStr)
        self.blocoText.config(state=DISABLED)

    def clear_text(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        self.blocoText.config(state=DISABLED)

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def destroy_frame(self):

        self.frameLocal.destroy()


class sub_Menu:
    def __init__(self, framePai, **kwargs):
        self.nome_op1 = kwargs.get('nome_B1', 'Opção 1')
        self.nome_op2 = kwargs.get('nome_B2', 'Opção 2')

        self.framePai = framePai

        self.menu = Menu(self.framePai, tearoff=0)
        self.menu.add_command(label=self.nome_op1, command=None)
        self.menu.add_command(label=self.nome_op2, command=None)

        # ~ self.bind(self.framePai)0

    def config_nome_B1(self, tit):
        # index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, label=tit)

    def config_nome_B2(self, tit):
        # index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, label=tit)

    def config_comando_B1(self, comando):
        # index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, command=comando)

    def config_comando_B2(self, comando):
        # index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, command=comando)

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def bind(self, pointer):
        pointer.bind("<Button-3>", self.popup)


class sub_CBox:
    def __init__(self, framePai, **kwargs):
        # kwargs:
        self.tit_CBox_text = kwargs.get('tit_CBox', 'Título')
        self.set_CBox_text = kwargs.get('set_CBox_default', '')
        self.CBox_state = kwargs.get('CBox_state', 'readonly')
        self.CBox_values = kwargs.get('CBox_values', ['Opção 1', 'Opção 2'])
        self.width = kwargs.get('width', 20)

        self.frameLocal = Frame(framePai)

        self.tit_CBox = Label(self.frameLocal, text=self.tit_CBox_text)
        self.tit_CBox.grid(row=0, column=0, sticky=W)

        self.var_CBox = StringVar()

        self.CBox = ttk.Combobox(self.frameLocal, textvariable=self.var_CBox, values=self.CBox_values, width=self.width)
        self.CBox.grid(row=1, column=0)

        self.CBox.set(self.set_CBox_text)
        self.CBox.config(state=self.CBox_state)

    def pointer_CBox(self):
        return (self.CBox)

    def pointer_tit_Cbox(self):
        return (self.tit_CBox)

    def config_CBox(self, **kwargs):
        self.CBox.config(kwargs)

    def config_Label(self, **kwargs):
        self.tit_CBox.config(kwargs)

    def add_value_CBox(self, lst):
        self.CBox.config(state="normal")
        list_values = list(self.CBox["values"])
        list_values.append(lst)
        self.CBox["values"] = list_values
        self.CBox.config(state="readonly")

    def define_values_CBox(self, lst):
        self.CBox["values"] = lst

    def retorna_escolha_CBox(self):
        return (self.var_CBox.get())

    def set_CBox_default(self, tit):
        if self.CBox['state'] != 'normal':
            state = self.CBox['state']
            self.CBox.config(state='normal')
            self.CBox.set(tit)
            self.CBox.config(state=state)
        else:
            self.CBox.set(tit)

    def config_CBox_state(self, estado):
        self.CBox.config(state=estado)

    def config_tit_CBox(self, titulo):
        self.tit_CBox.config(text=titulo)

    def finaliza(self):
        self.frameLocal.destroy()

    def grid_frame(self, **kwargs):
        # kwargs:
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def insere_nova_CBox(self, CBox):
        self.CBox.destroy()
        self.CBox = CBox(self.frameLocal)
        self.CBox.grid(row=2, column=3, padx=5)


