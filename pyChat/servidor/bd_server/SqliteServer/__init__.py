import sqlite3

class sqliteConn:
    def __init__(self, nameDb: str = "bd_server\sqliteServer\BD_prog.db") -> object:
        """

        :rtype: object
        """
        try:
            self.conn = sqlite3.connect(nameDb)
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            # self.data = self.cursor.fetchone()
            self.conn.close()
            self.con_status = False
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __conect_BD__(self):
        try:
            if (self.con_status == False):
                self.conn = sqlite3.connect("bd_server\sqliteServer\BD_prog.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()
            else:
                raise Exception('Conexão indisponível ou já em uso')
                pass
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()

    def __select_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __lastrowid__(self):
        return self.cursor.lastrowid

    def __execute_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return elem
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __execute_transaction__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                #EXECUTAR A TRANSAÇÃO SEM TUPLA
                pass
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            return self.__expt_msg__(Expt)


    def __select_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return lst
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __execute_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __execute_commit__(self, sql='', tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return 0
        except Exception as Expt:
            return self.__expt_msg__(Expt)

    def __strip_id__(self, idd, tipo='int'):
        idd = str(idd)
        idd = idd.strip(')').strip('(').strip(",")

        if tipo == 'int':
            idd = int(idd)
            return (idd)
        elif tipo == 'str':
            return (idd)
        else:
            raise Exception('Argumento: ', tipo, ' não reconhecido, precisa ser "str" ou "int"')

    def finaliza_conexao(self):
        self.__disconect_BD__()

    def __expt_msg__(self, Expt: object) -> object:
        print('Erro no banco de dados: ')
        self.finaliza_conexao()
        print(str(Expt))
        print(type(Expt))
        print('É do tipo Except? -> '+str(isinstance(Expt, Exception)))
        return Expt