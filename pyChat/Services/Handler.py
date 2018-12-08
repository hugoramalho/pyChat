from pyChat.Services import Mappers
from pyChat.Models import Models
from pyChat.Services import DTP, Requests, Responses


def MyRequestHandler(dictRequest: dict):

    request = Requests.DataTransferEval(dictRequest).eval()

    if isinstance(request, Requests.RequestLogin):
        login = request.user

        feedback = Mappers.UserMapper().login(login)
        print('tipo aqui' +str(feedback))
        if isinstance(feedback, Models.user):
            # login OK
            response = Responses.ResponseLogin(feedback)
            return response
        elif isinstance(feedback, Exception):
            # ROTINA DE ENCAPSULAMENTO DE ERRO
            response = DTP.InternalExceptions(Requests.RequestLogin(), feedback)
            return response

    elif isinstance(request, Requests.RequestRetrieveFriends):
        user = request.user
        feedback = Mappers.UserMapper().retrieveFriends(user)
        if isinstance(feedback, Models.LstUsers):
            response = Responses.ResponseRetrieveFriends(feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(Requests.RequestRetrieveFriends(), feedback)
            return response

    elif isinstance(request, Requests.RequestRetrieveChat):
        feedback = Mappers.ChatMapper().retrieveChat(request.friendship)
        if isinstance(feedback, Models.LstMessages):
            response = Responses.ResponseRetrieveChat(feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(Requests.RequestRetrieveChat(), feedback)
            return response

    elif isinstance(request, Requests.RequestSendMessage):
        feedback = Mappers.ChatMapper().insertMessage(request.message)
        if isinstance(feedback, Models.Message):
            # MENSAGEM ALTERA O STATUS DE RECEPÇÃO NO CLIENTE REMETENTE PARA TRUE
            # MENSAGEM É ENVIADA (ASSÍNCRONA) PARA O CLIENTE DESTINATÁRIO
            response = Responses.ResponseSendMessage(feedback)
            return response
        elif isinstance(feedback, Exception):
            # ROTINA DE TRATAMENTO DE ERRO
            # STATUS DE RECEPÇÃO DO CLIENTE SE MANTÉM INALTERADO (FALSE)
            response = DTP.InternalExceptions(Responses.ResponseSendMessage(), feedback)
            return response

    elif isinstance(request, Requests.RequestNewUser):
        feedback = Mappers.UserMapper().newUser(request.user)
        if isinstance(feedback, Models.user):
            response = Responses.ResponseNewUser(feedback)
            return response
        elif isinstance(feedback, Exception):
            # TRATAR OS ERROS AQUI
            response = DTP.InternalExceptions(Responses.ResponseNewUser(), feedback)
            return response

    elif isinstance(request, Requests.RequestNamesLike):
        feedback = Mappers.UserMapper().namesLike(request.user, request.namesLike)
        if isinstance(feedback, Models.LstUsers):
            response = Responses.ResponseNamesLike(feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(Responses.ResponseNamesLike(), feedback)
            return response

    elif isinstance(request, Requests.RequestAddFriend):
        feedback = Mappers.UserMapper().addFriend(request.user, request.friendEmail)
        if isinstance(feedback, Models.Friendship):
            response = Responses.ResponseAddFriend(feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(Requests.RequestAddFriend(), feedback)
            return response

    elif isinstance(request, Requests.RequestFriendshipAcepted):
        feedback = Mappers.UserMapper().friendshipAcepted(request.friendship)
        if isinstance(feedback, Models.Friendship):
            response = Responses.ResponseFriendshipAcepted(feedback)
            return response
        elif isinstance(feedback, Exception):
            response = DTP.InternalExceptions(Requests.RequestAddFriend(), feedback)
            return response