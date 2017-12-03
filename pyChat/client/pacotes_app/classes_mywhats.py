from datetime import datetime


class mensagem:
    """LEMBVRAR QUE O datetime nao é serializavel pelo JSON"""
    def __init__(self, **kwargs):
        #ABAIXO É VERIFICADO SE O KWARGS É UM INICIALIZADOR VÁLIDO PARA A CLASSE:
        
        isoformat =  '%Y-%m-%d %H:%M:%S.%f'
        self.data_hora = datetime.strptime(kwargs.get('data_hora', ''), isoformat)
        self.id_user = kwargs.get('id_user', '')#lembrar de colocar quem é o usuario da sessao ativa
        self.remet = kwargs.get('remet', '')
        self.id_rem = kwargs.get('id_rem', '')
        self.dest = kwargs.get('dest', '')
        self.id_dest = kwargs.get('id_dest', '')
        self.conteudo = kwargs.get('conteudo', '')
        self.tipo = self.__class__.__name__



    #~ @hora_data.setter
    #~ def nome(self, hora_data):
        #~ #LEMBRAR DE FAZER A VERIFICAÇÃO
        #~ self.hora_data = hora_data
        
    def __setHora__(self):
        pass
        
    def __iter__(self):
        yield 'data_hora', self.data_hora.isoformat(' ')
        yield 'remet', self.remet
        yield 'id_rem', self.id_rem
        yield 'dest',  self.dest
        yield 'id_dest', self.id_dest
        yield 'conteudo', self.conteudo
        yield 'tipo', self.tipo

    def __str__(self):
        return(str(dict(self)))



    def __eq__(self, obj):
        return (self.data_hora == obj.data_hora)

    def __ne__(self, obj):
        return (self.data_hora != obj.data_hora)

    def __lt__(self, obj):
        return (self.data_hora < obj.data_hora)

    def __le__(self, obj):
        return (self.data_hora <= obj.data_hora)

    def __gt__(self, obj):
        return (self.data_hora > obj.data_hora)

    def __ge__(self, obj):
        return (self.data_hora >= obj.data_hora)

    def __repr__(self):
        return(str(dict(self)))

    def dic_db(self):
        dic = {}
        dic['data_hora'] = self.data_hora.isoformat(' ')
        dic['conteudo'] = self.conteudo
        dic['id_dest'] = self.id_dest
        dic['id_rem'] = self.id_rem
        return(dic)



    def dic_treeview(self):
        elem1 = str(self.remet)+' '+ str(self.data_hora.day)+'/'+ str(self.data_hora.month)+'/'+ str(self.data_hora.year) +' às '+ str(self.data_hora.hour) + ':'+ str(self.data_hora.minute)
        elem2 = self.conteudo
        
        dic_treeView = {}
        dic_treeView['text'] = elem1
        dic_treeView['values'] = [elem2]
        dic_treeView['index'] = 'end'
        #~ print('\nDIC  ',dic_treeView)
        return(dic_treeView)




class contato:
    def __init__(self, **kwargs):
        self.id_contato = kwargs.get('id_contato', '')
        self.nome_contato = kwargs.get('nome_contato', '')

    def __str__(self):
        return('Contato: ' + str(self.nome_contato) +' | id: ' + str(self.id_contato))
        
        
    def __repr__(self):
        return('Contato: ' +  str(self.nome_contato) +' | id: ' + str(self.id_contato))
        

    def dic_treeview(self):
        dic_treeView ={}
        dic_treeView['idd'] = self.id_contato
        dic_treeView['text'] = self.nome_contato
        dic_treeView['values'] = ['']

        return(dic_treeView)



class usuario:
    
    def __init__(self, **kwargs):
        self.tipo = self.__class__.__name__
        self._nome = kwargs.get('nome', '')
        self._senha = kwargs.get('senha', '')
        self._idd = kwargs.get('id', '')
        
    
    def update(self, **kwargs):
        #LEMBRAR DE FAZER VERIFICAÇÕES
        self._nome = kwargs.get('nome', self._nome)
        self._senha = kwargs.get('senha', self._senha)

    @property
    def idd(self):
        return self._idd
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def senha(self):
        return self._y

    @senha.setter
    def senha(self, senha):
        self._senha = senha



class log_in:
    #PODE SER QUE NAO SIRVA
    def __init__(self, **kwargs):
        self.usuario = kwargs.get('usuario', 'teste')
        self.senha = kwargs.get('senha', '$$$$')
        self.tipo = self.__class__.__name__


    def __iter__(self):
        yield 'usuario', self.usuario
        yield 'tipo', self.tipo
        yield 'senha', str(self.senha)



class lst_contatos(list):
    """
    A PRESENTE CLASSE RECEBE UMA LISTA DE DICIONARIOS REPRESENTANDO MENSAGENS
    EM SEGUIDA PERCORRE A LISTA DE DICIONÁRIOS E INSTANCIA AS MENSAGENS POR MEIO DOS DICONARIOS
    OU SEJA, O CONSTRUTOR DA CLASSE MENSAGEM RECEBE COMO PARAMETRO UM DICIONARIO COM OS ATRIBUTOS
    """
    def __init__(self, **kwargs):
        
        super().__init__()
        lst_contat = kwargs.get('lst_contatos', [])
        #~ print('dentro do construtor', lst_contat)

        
        if lst_contat != []: 
            for dic_elem in lst_contat:
                contato_aux = contato(**dic_elem)
                self.append(contato_aux)
        else:
            pass
            
    
    def busca_id(self, idd):
        for elem in self:
            if type(idd) != int:
                idd = int(idd)
            
            if elem.id_contato == idd:
                return(elem)
        
    def lst_treeview(self):
        lst_treeview =[]
        try:
            for elem in self:
                dic_aux = elem.dic_treeview()
                lst_treeview.append(dic_aux)
            return(lst_treeview)
        except Exception as Expt:
            print(Expt)
            pass
        
    #~ def __append__(self, elem):
        #~ if isinstance(elem, mensagem) == True:
            #~ self.append(elem)
        #~ else:
            #~ return(None)


class lst_mensagem(list):
    """
    A PRESENTE CLASSE RECEBE UMA LISTA DE DICIONARIOS REPRESENTANDO MENSAGENS
    EM SEGUIDA PERCORRE A LISTA DE DICIONÁRIOS E INSTANCIA AS MENSAGENS POR MEIO DOS DICONARIOS
    OU SEJA, O CONSTRUTOR DA CLASSE MENSAGEM RECEBE COMO PARAMETRO UM DICIONARIO COM OS ATRIBUTOS
    """
    def __init__(self, *args):
        
        super().__init__()
        lst_msg = args
        #~ print('\n\n\n\n\n', args)
        
        if len(lst_msg) > 0:
            for dic_elem in lst_msg:
                
                msg = mensagem(**dic_elem)
                self.append(msg)
            self.reverse()
        else:
            pass
    

        
    def lst_treeview(self):
        try:
            lst_treeview =[]
            for elem in self:
                dic_aux = elem.dic_treeview()
                lst_treeview.append(dic_aux)
            return(lst_treeview)
        except Exception as Expt:
            print(Expt)
            pass
            
    #~ def __append__(self, elem):
        #~ if isinstance(elem, mensagem) == True:
            #~ self.append(elem)
        #~ else:
            #~ return(None)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
