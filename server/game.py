"""
host the main loop for a game
Should not have any networking code in here

"""



class Game:
    def __init__(self,room):
        self.room=room
        self.time=0
        self.game_over=False
        self.snapshot={"test_text":""}
        self.test_text=""

    def tick(self):
        self.time+=1
        print (self.time)
        if not(self.game_over):
            self.room.end_game()
            return



        if self.time >100000000:
            self.game_over=True


        self.update_snapshot()

    def update_snapshot():
        self.snapshot["test_text"]=self.test_text