"""
This is the game_room class it controls starting and stopping of games

Can have some networking code in here

"""
from game import Game
from tornado import  ioloop

class Game_room:
    def __init__(self):
        self.players=[]
        self.current_game=None
        self.game_timer=None

    def start_game(self):
        self.current_game=Game(self)
        self.game_timer= ioloop.PeriodicCallback(self.current_game.tick,15) # every 15 ms call the main game loop
        self.game_timer.start()
        

    def end_game(self):
        print("stopping game")
        self.game_timer.stop()
        self.game_timer=None
        self.current_game=None

    def snapshot(self):
        if self.current_game:
            return self.current_game.snapshot
        else:
            return {}
