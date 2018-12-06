from pyChat.servidor.ServerPacks.Models import Models
from pyChat.servidor.ServerPacks.Services import Mappers, DTP


def MyRequestHandler(dictRequest: dict):
    requestName = dictRequest['request']

    if requestName == 'login':
        login = Models.Login().fromJson(dictRequest)

        feedback = Mappers.UserMapper().login(login)
        if isinstance(feedback, Models.user):
            #login OK
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            #ROTINA DE ENCAPSULAMENTO DE ERRO
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'retrieve_friends':
        user = Models.user().fromJson(dictRequest)
        feedback = Mappers.UserMapper().retrieveFriends(user)
        if isinstance(feedback, Models.LstUsers):
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'retrieve_chat':
        userId = dictRequest['userId']
        friendId = dictRequest['friendId']

        feedback = Mappers.ChatMapper().retrieveChat(userId, friendId)
        if isinstance(feedback, Models.LstMessages):
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'send_message':
        message = Models.Message().fromJson(dictRequest)
        feedback = Mappers.ChatMapper().insertMessage(message)
        if isinstance(feedback, Models.Message):
            #MENSAGEM ALTERA O STATUS DE RECEPÇÃO NO CLIENTE REMETENTE PARA TRUE
            #MENSAGEM É ENVIADA (ASSÍNCRONA) PARA O CLIENTE DESTINATÁRIO
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            #ROTINA DE TRATAMENTO DE ERRO
            #STATUS DE RECEPÇÃO DO CLIENTE SE MANTÉM INALTERADO (FALSE)
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'new_user':
        newUser = Models.user().fromJson(dictRequest)
        feedback = Mappers.UserMapper().newUser(newUser)
        if isinstance(feedback, Models.user):
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            #TRATAR OS ERROS AQUI
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'namesLike':
        namesLike = dictRequest['namesLike']
        user = Models.user().fromJson(dictRequest['user'])
        feedback = Mappers.UserMapper().namesLike(user, namesLike)
        if isinstance(feedback, Models.LstUsers):
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(requestName, feedback)
            return response

    elif requestName == 'addFriend':
        friendEmail = dictRequest['friendEmail']
        user = Models.user().fromJson(dictRequest['user'])
        feedback = Mappers.UserMapper().addFriend(friendEmail, user)
        if isinstance(feedback, Models.user):
            response = DTP.Request(requestName, feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(requestName, feedback)
            return response