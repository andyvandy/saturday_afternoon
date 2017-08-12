"""
host the main loop for a game
Should not have any networking code in here

"""



class Game:
    def __init__(self,room):
        self.room=room
        self.tick=0
        self.game_over=False

    def tick():
        self.tick+=1
        if not(self.game_over):
            self.room.end_game()
            return

        if self.tick >100:
            self.game_over=True
