"""Pacote reservado ao banco de dados do programa, que está contido no servidor"""

__all__ = ['bd_prog', 'server_requests']

'''
    O módulo bd_prog guarda todas as API's de comunicação com o sqlite, encapsuladas em uma classe.
    A classe, por meio das API's molda o banco de dados do programa, contendo funções de busca e inserção.
    
    O módulo server_requests guarda as funções que fazem o intermédio do servidor com o banco de dados.
    Dessa forma, o handler() do servidor apenas precisa chamar as funções contidas em server_requests,
    sem conhecer como o banco de dados está estruturado. 
'''
