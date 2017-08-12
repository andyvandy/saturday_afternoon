"""
Call this file to play the game
sources:
    -https://github.com/ilkerkesen/tornado-websocket-client-example/blob/master/client.py
"""
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor   # `pip install futures` for python2

import json

import game_files
from game_files.main import Game

ADDRESS="ws://localhost:8888"
MAX_WORKERS=16

class Client(object):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    def __init__(self, url, timeout):

        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.game = None
        self.start_game()
        self.connect()
        self.ioloop.start()


    @run_on_executor
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
       # self.send_events({"attack":"fun increased by 10"})
        while True:
            msg = yield self.ws.read_message()
            self.handle_msg(json.loads(msg))
            if msg is None:
                print( "connection closed")
                self.ws = None
                break
    @gen.coroutine
    def handle_msg(self,msg):
        if self.game == None: return
       # return
        print("got msg",msg)
        #parsed_msg= json.loads(msg)
       
        if "snapshot" in msg:
            print("got snapshot")
            self.game.update_world_state(msg["snapshot"])
        else:
            print("sadsadasdasd")
    def send_events(self,msg):

        print("Sending json msg",msg)
        json_msg=json.dumps({"event":self.game.events})
        self.game.events=[]
        self.ws.write_message(json_msg)



if __name__=="__main__":
    client = Client(ADDRESS, 5)
    event_timer= PeriodicCallback(client.send_events,60) # every 15 ms call the main game loop
    event_timer.start()
