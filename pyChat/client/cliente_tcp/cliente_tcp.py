import json
import socket

from pyChat.client.cliente_tcp.async_tcp import client2


class cliente_tcp:
    def __init__(self, controller, **kwargs):
        self.host = kwargs.get('host', '127.0.0.1')     # Endereco IP do Servidor
        self.port = kwargs.get('port', 3333)           # Porta que o Servidor está
        self.dest = (self.host, self.port)
        self.controller = controller
        self.assincClient = client2.ClientProtocol(self.controller)


    def connect(self):
        try:
            self.assincClient = client2.ClientProtocol(self.controller)
            self.assincClient.connect()
        except Exception as Expt:
            self.controller.exceptionHandler(Expt)

    def disconnect(self):
        self.assincClient.disconnect()



    def sendRequest(self, obj):
        try:
            if self.assincClient.connStatus is False:
                self.connect()
                if self.assincClient.connStatus is True:
                    print('AQUI YU')
                    print(obj)
                    data = json.dumps(obj)
                    data.encode()
                #   self.assincClient.send_message(data)
                    self.assincClient.transport.write(data.encode('utf-8'))
        except Exception as Expt:
            self.controller.exceptionHandler(Expt)