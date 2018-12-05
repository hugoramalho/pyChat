"""Aqui ficam guardadas as funções de cada request"""


from . import Mappers
# Uma conexão com o banco de dados é instanciada:



def carrega_conv_handle(**kwargs):
    dic_retorno = {}
    dic_retorno['req'] = 'carrega_conversa'
    dic_retorno['id_user'] = kwargs['id_user']
    dic_retorno['id_contato'] = kwargs['id_contato']
    dic_retorno['lst_conv'] = Mappers.ChatMapper().retrieveChat(kwargs['id_user'], kwargs['id_contato'])
    print('server_requests '+str(dic_retorno))
    return dic_retorno


def carrega_conv_handle(**kwargs):
    dic_retorno = {}
    dic_retorno['req'] = 'carrega_conversa'
    dic_retorno['id_user'] = kwargs['id_user']
    dic_retorno['id_contato'] = kwargs['id_contato']
    dic_retorno['lst_conv'] = Mappers.ChatMapper().retrieveChat(kwargs['id_user'], kwargs['id_contato'])
    print('server_requests '+str(dic_retorno))
    return dic_retorno

def envio_msg_handle(**kwargs):
    dic_feedback = {}
    dic_feedback['recipId'] = kwargs['recipId']
    dic_feedback = Mappers.ChatMapper().insertMessage(**kwargs)
    dic_feedback['req'] = 'recp_msg'
    return dic_feedback


def carrega_contat_handle(**kwargs):
    dic_retorno = {}
    dic_retorno['lst_contatos'] = Mappers.UserMapper().retrieveFriends(kwargs['id_user'])
    dic_retorno['req'] = 'carrega_contatos'
    return dic_retorno


def login_handle(**kwargs):
    dic_feedback = Mappers.UserMapper().login(kwargs['userEmail'], kwargs['password'])
    dic_feedback['req'] = 'login'
    return dic_feedback


def novo_user_handle(**kwargs):
    # o método do BD abaixo, tenta adicionar um novo usuário,
    # E retorna um dicionário contendo o feedback da operação
    # Caso já exista um usuário com o mesmo nome, um erro é tratado
    # E o dicionário na posição 'Erro' descreve o ocorrido
    dic_feedback = Mappers.UserMapper().newUser(kwargs['userName'], kwargs['userEmail'], kwargs['password'])
    dic_feedback['req'] = 'novo_user_response'
    return dic_feedback


def busca_contato_handle(**kwargs):
    dic_retorno = Mappers.UserMapper().namesLike(**kwargs)
    dic_retorno['req'] = 'namesLike'
    return dic_retorno

def addFriend(**kwargs):
    userEmail = kwargs.get('userEmail')
    friendEmail = kwargs.get('friendEmail')
    feedback = Mappers.UserMapper().addFriend(userEmail,friendEmail)
    feedback['req'] = 'addFriend'
    return feedback
