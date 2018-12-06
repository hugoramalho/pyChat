from pyChat.servidor.ServerPacks.ThreadedServer import *
import sys



if __name__ == "__main__":
    server = ThreadedTCPServer(('127.0.0.1', 3333), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)

    try:
        server_thread.start()
        print('<< Server online >>')
    except KeyboardInterrupt:
        print('<< Server offline >>')
        sys.exit(0)