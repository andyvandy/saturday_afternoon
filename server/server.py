"""
call this file to run the game server
This file does not contain the game logic just the communications logic

"""
DEBUG=True
PORT=8888

from tornado import websocket, web, ioloop

clients = []


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in clients:
            if DEBUG : print("client connected",self)
            clients.append(self)

    def on_close(self):
        if self in clients:
            clients.remove(self)

def main():
    app = web.Application([(r'/', SocketHandler)])
    app.listen(PORT)
    print("listiening on {0}".format(PORT))
    ioloop.IOLoop.current().start()



if __name__=="__main__":
    main()