import asyncio
import json
from tkinter import *
import threading
from functools import partial
import logging

class wd_Entry(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.label = kwargs.get('label', 'Título')
        self.tit_Entry_text = kwargs.get('entry_Label', self.label)
        self.set_Entry_default = kwargs.get('set_Entry_default', '')
        self.state_Entry = kwargs.get('state', 'normal')
        self.state_Entry = kwargs.get('state_Entry', self.state_Entry )
        self.width_Entry = kwargs.get('width', 20)

        self.frameLocal = Frame(framePai)
        self.entry_Label = Label(self.frameLocal, text=self.tit_Entry_text)
        self.var_Entry = StringVar()
        self.entry = Entry(self.frameLocal, textvariable=self.var_Entry, width=self.width_Entry,
                               state=self.state_Entry)
        self.insert_text(self.set_Entry_default)

    def wd_state(self, state):
        self.entry.config(state = state)

    def config_Entry(self, **kwargs):
        self.entry.config(kwargs)

    def get_text(self):
        return self.var_Entry.get()

    def insert_text(self, txt):
        if self.entry['state'] != 'normal':
            state = self.entry['state']
            self.entry.config(state='normal')
            self.limpa_entr()
            self.entry.delete(0, "end")
            self.entry.insert('end', txt)
            self.entry.config(state=state)
        else:
            self.limpa_entr()
            self.entry.insert('end', txt)

    def config_Entry_state(self, estado):
        self.entry.config(state=estado)

    def config_tit_Entry(self, titulo):
        self.entry_Label.config(text=titulo)

    def finaliza(self):
        self.frameLocal.destroy()

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 2)
        padx = kwargs.get('padx', 2)

        self.entry_Label.grid(row=0, column=0, sticky=W, columnspan=columnspan)
        self.entry.grid(row=1, column=0, sticky=sticky, columnspan=columnspan)
        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def limpa_entr(self):
        self.entry.delete(0, "end")

class wd_Text(Frame):

    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.tit = kwargs.get('label', 'Título')
        self.state = kwargs.get('state', NORMAL)
        self.width = kwargs.get('width', 50)
        self.height = kwargs.get('height', 4)
        self.scrollbarx = kwargs.get('scrollbarx', True)
        self.scrollbary = kwargs.get('scrollbary', True)
        self.bd = kwargs.get('bd', 3)

        # Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frameLocal = Frame(framePai)

        self.text_Label = Label(self.frameLocal, text=self.tit)
        self.text_Label.grid(row=0, column=0, sticky=W)

        self.text = Text(self.frameLocal, insertborderwidth=5, bd=self.bd, font="Arial 9", wrap=WORD,
                         width=self.width, height=self.height, state=self.state, autoseparators=True)
        self.text.grid(row=1, column=0)

        self.__scrollbar_constr__()

        # ~ self.separator1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        # ~ self.separator1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")

    def config_Text(self, **kwargs):
        self.text.config(kwargs)

    def get_text(self):
        text = self.text.get(1.0, "end")
        return (text)

    def wd_state(self, state):
        self.text.config(state = state)


    def __scrollbar_constr__(self):
        if self.scrollbarx == True:
            self.scrollbarX = Scrollbar(self.frameLocal, command=self.text.xview, orient=HORIZONTAL)
            self.scrollbarX.grid(row=2, column=0, sticky=E + W)
            self.text.config(xscrollcommand=self.scrollbarX.set)

        if self.scrollbary == True:
            self.scrollbarY = Scrollbar(self.frameLocal, command=self.text.yview, orient=VERTICAL)
            self.scrollbarY.grid(row=1, column=1, sticky=N + S)
            self.text.config(yscrollcommand=self.scrollbarY.set)

    def delete(self, index1 = 1, index2 = END):
        self.text.delete(index1, index2)

    def insert_text(self, txtStr, clean):
    # TODO ALTERAR O METODO PARA RECEBER OS DOIS PARAMETROS:
    # def insert_text(self, param = 1, txtStr):
        if self.text['state'] != NORMAL:
            state = self.text['state']
            self.text.config(state=NORMAL)
            if clean == True:
                self.text.delete(1.0, END)
            self.text.insert(1.0, txtStr)
            self.text.config(state=DISABLED)
            self.text.config(state=state)
        else:
            if clean == True:
                self.text.delete(1.0, END)
            self.text.insert(1.0, txtStr)

    def clear_text(self):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.config(state=DISABLED)

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

class chatFrame:
    def __init__(self, framePai, controller):
        self.controller = controller
        
        self.text = wd_Text(framePai)
        self.text.grid_frame(column=2)
        self.entrPort = wd_Entry(framePai, label='to port. . . ')
        self.entrPort.grid_frame(row=0)
        self.entrMsg = wd_Entry(framePai, label='Message:')
        self.entrMsg.grid_frame(row=1)
        self.send = Button(framePai, text = 'send', command = self.sendButton)
        self.send.grid()
        
    def insert_msg(self, msg, fromPort):
        self.text.insert_text('Message from port '+str(fromPort)+': '+msg, False)
        
    def sendButton(self):
        port = int(self.entrPort.get_text())
        msg = self.entrMsg.get_text()
        self.controller.sendMsg(port, msg)

class AppController:
    def __init__(self, tk):
        
        self.chatFrame = chatFrame(tk, self)
        self.conn = ClientProtocol(self)
        self.conn.connect()
        
    def sendMsg(self, port, msg):
        message = json.dumps({'type': 'message_outcome', 'port': port, 'message':msg},
                         separators=(',', ':'))
        #self.send_message(message)
        self.conn.transport.write(message.encode('utf-8'))
     
    
    def addMsg(self, msg, fromPort):
        self.chatFrame.insert_msg(msg, fromPort)
        
    def handle(self, data):
        request = json.loads(data.decode())
        if request['type'] == 'message_income':
            fromPort = request['fromPort']
            message = request['message']
            self.addMsg(message, fromPort)   

class RequestHandler:
    def __init__(self, serviceController=None):
        self.controller = serviceController
        
    def handle(data):
        request = json.loads(data.decode())
        if request['type'] == 'message_income':
            fromPort = request['fromPort']
            message = request['message']
            self.controller.addMsg(message, fromPort)

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
        loop = asyncio.get_event_loop()  # Pulls the new event loop because that is who launched this coroutine
        loop.set_debug(True)
        coro = loop.create_connection(lambda: self,'127.0.0.1', 3333)
        _, proto = loop.run_until_complete(coro)

    def _run(self, loop):
        asyncio.set_event_loop(loop)

        loop.run_forever()

    def connect(self):
        try:
            ioloop = asyncio.new_event_loop()
            asyncio.run_coroutine_threadsafe(self._connect(), loop=ioloop)  # Schedules connection
            t = threading.Thread(target=partial(self._run, ioloop))
            t.daemon = True  # won't hang app when it closes
            t.start()  # Server will connect now
            asyncio.async(self._send_messages())  # Or asyncio.ensure_future if using 3.4.3+
        except Exception as Expt:
            return Expt

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
            raise Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)')

    @asyncio.coroutine
    def send_message(self, data):
        """ Feed a message to the sender coroutine. """
        try:
            yield from self.queue.put(data)
        except Exception as Expt:
            raise Exception('Connection failure: ConnectionRefusedError: [Errno 10061] Connect call failed (127.0.0.1, 3333)')

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
        

@asyncio.coroutine
def feed_messages(protocol):
    """ An example function that sends the same message repeatedly. """
    message = json.dumps({'type': 'subscribe', 'channel': 'sensor', 'message':'',},
                         separators=(',', ':'))
    while True:
        yield from protocol.send_message(message)
        yield from asyncio.sleep(1)



if __name__ == '__main__':
    tk = Tk()
  
    app = AppController(tk)

    tk.mainloop()
 
        

