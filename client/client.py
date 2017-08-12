"""
Call this file to play the game
sources:
    -https://github.com/ilkerkesen/tornado-websocket-client-example/blob/master/client.py
"""
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect
import json

import game_files
from game_files.main import Game

class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.game = None
        self.start_game()
        self.connect()
        PeriodicCallback(self.keep_alive, 20000, io_loop=self.ioloop).start()
        self.ioloop.start()

    def start_game(self ):
        self.game = Game()
        self.game.start()


    @gen.coroutine
    def connect(self):
        print( "trying to connect")
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception as e:
            print( "connection error")
        else:
            print( "connected")
            self.run()

    @gen.coroutine
    def run(self):
        self.send_event({"attack":"fun increased by 10"})
        while True:
            msg = yield self.ws.read_message()
            if msg is None:
                print( "connection closed")
                self.ws = None
                break

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")

    

    def send_event(self,message):
        print("Sending json msg",message)
        json_msg=json.dumps({"event":message})
        self.ws.write_message(json_msg)



if __name__=="__main__":
    client = Client("ws://localhost:8888", 5)