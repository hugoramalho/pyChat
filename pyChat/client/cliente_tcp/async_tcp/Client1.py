import asyncio
import time


class SimpleChatClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info("peername")
        print("connection_made: {}".format(self.peername))


    def data_received(self, data):
        print("data_received: {}".format(data.decode()))


    def connection_lost(self, ex):
        print("connection_lost: {}".format(self.peername))

