"""
This is the game_room class it controls starting and stopping of games

Can have some networking code in here

"""
from game import Game

class Game_room:
    def __init__(self):
        self.players=[]
        self.current_game=None
        self.game_timer=None

    def start_game(self):
        self.current_game=Game(self)
        game_timer= tornado.ioloop.PeriodicCallback(self.current_game.tick,15) # every 15 ms call the main game loop
        game_timer.start()
        

    def end_game(self):
        self.game_timer.stop()
        self.game_timer=None
        self.current_game=None

