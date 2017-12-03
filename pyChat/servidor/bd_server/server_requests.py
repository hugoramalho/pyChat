"""Aqui ficam guardadas as funções de cada request"""

#O banco de dados é importato
from . import bd_prog as BD
# Uma conexão com o banco de dados é instanciada:
bd_prog = BD.conexao_BD_prog()


def busca_contat_handle(**kwargs):
    ###
    dic_retorno = bd_prog.fetchall_contatos_like(**kwargs)
    return (dic_retorno)


def carrega_conv_handle(**kwargs):
    dic_retorno = {}
    dic_retorno['id_user'] = kwargs['id_user']
    dic_retorno['id_contato'] = kwargs['id_contato']
    dic_retorno['lst_conv'] = bd_prog.fetch_mensagens(kwargs['id_user'], kwargs['id_contato'])
    return dic_retorno


def envio_msg_handle(**kwargs):
    dic_feedback = bd_prog.insere_msg(**kwargs)
    return dic_feedback


def carrega_contat_handle(**kwargs):
    dic_retorno = {}
    dic_retorno['lst_contatos'] = bd_prog.fetchall_contatos(kwargs['id_user'])
    return dic_retorno


def login_handle(**kwargs):
    nome_user = kwargs['nome']
    dic_feedback = bd_prog.fetch_usuario(nome_user)
    return dic_feedback


def novo_user_handle(**kwargs):
    # o método do BD abaixo, tenta adicionar um novo usuário,
    # E retorna um dicionário contendo o feedback da operação
    # Caso já exista um usuário com o mesmo nome, um erro é tratado
    # E o dicionário na posição 'Erro' descreve o ocorrido
    dic_feedback = bd_prog.insere_user(**kwargs)
    return dic_feedback


def busca_contato_handle(**kwargs):
    dic_retorno = bd_prog.fetchall_contatos_like(**kwargs)
    return dic_retorno