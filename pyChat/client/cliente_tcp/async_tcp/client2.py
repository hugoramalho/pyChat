import asyncio
import json
from tkinter import *
import threading
from functools import partial
import logging




logging.getLogger("asyncio").setLevel(logging.WARNING)

class ClientProtocol(asyncio.Protocol):
    def __init__(self, requestHandler):
        self.transport = None
        #self.loop = loop
        self.queue = asyncio.Queue()
        self._ready = asyncio.Event()

        self.handler = requestHandler


    @asyncio.coroutine
    def _connect(self):
        try:
            loop = asyncio.get_event_loop()  # Pulls the new event loop because that is who launched this coroutine
            loop.set_debug(True)
            coro = loop.create_connection(lambda: self,'127.0.0.1', 3333)
            _, proto = loop.run_until_complete(coro)
        except:
            self.handler.exceptionHandler(Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)'))

    def _run(self, loop):
        try:
            asyncio.set_event_loop(loop)
            loop.run_forever()
        except:
            self.handler.exceptionHandler(Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)'))

    def connect(self):
        try:
            ioloop = asyncio.new_event_loop()

            #asyncio.run_coroutine_threadsafe(self._connect(), loop=ioloop)  # Schedules connection
            asyncio.gather(self._connect(), loop=ioloop, return_exceptions=True)
            t = threading.Thread(target=partial(self._run, ioloop))
            t.daemon = True  # won't hang app when it closes
            t.start()  # Server will connect now
            asyncio.async(self._send_messages())  # Or asyncio.ensure_future if using 3.4.3+
        except Exception as Expt:
            print('dentro da thread')
            raise Expt

    @asyncio.coroutine
    def _send_messages(self):
        """ Send messages to the server as they become available. """
        try:
            yield from self._ready.wait()
            print("Ready!")
            while True:
                data = yield from self.queue.get()
                self.transport.write(data.encode('utf-8'))
                print('Message sent: {!r}'.format(message))
        except Exception as Expt:

            return Expt

    def connection_made(self, transport):
        """ Upon connection send the message to the
        server

        A message has to have the following items:
            type:       subscribe/unsubscribe
            channel:    the userName of the channel
        """
        try:
            self.transport = transport
            print("Connection made.")
            self._ready.set()
        except Exception as Expt:
            print('DENTRO DA THREAD')
            self.handler.exceptionHandler(Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)'))

    @asyncio.coroutine
    def send_message(self, data):
        """ Feed a message to the sender coroutine. """
        try:
            yield from self.queue.put(data)
        except Exception:
            print('DENT TREAD')
            self.handler.exceptionHandler(Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)'))

    def data_received(self, data):
        """ After sending a message we expect a reply
        back from the server

        The return message consist of three fields:
            type:           subscribe/unsubscribe
            channel:        the userName of the channel
            channel_count:  the amount of channels subscribed to
        """
        print('Message received: {!r}'.format(data.decode()))
        if self.handler is not None:
            self.handler.handle(data)

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()
