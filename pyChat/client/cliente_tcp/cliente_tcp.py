import json
from pyChat.client.cliente_tcp.async_tcp import client2


class cliente_tcp:
    def __init__(self, controller, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')  # Endereco IP do Servidor
        self.port = kwargs.get('port', 3333)  # Porta que o Servidor está
        self.dest = (self.host, self.port)
        self.con_status = False
        self.controller = controller
        self.client_t = client2.ClientProtocol(controller)

    def conecta(self):
        try:
            self.client_t.connect()
        except Exception as Expt:

            return Expt

    def sendRequest(self, obj):
        try:
            print('Enviando req: ', obj)
            data = json.dumps(obj)
            data.encode()
            # self.client_t.send_message(data)
            self.client_t.transport.write(data.encode('utf-8'))
        except Exception as Expt:
            return Expt