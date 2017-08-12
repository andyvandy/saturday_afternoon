"""
host the main loop for a game
Should not have any networking code in here

"""



class Game:
    def __init__(self,room):
        self.room=room
        self.time=0
        self.game_over=False
        self.snapshot={"test_field":self.time}


    def tick(self):
        self.time+=1
        #print (self.time)
        if self.game_over:
            self.room.end_game()
            return



        if self.time >100000000:
            print ("game over at ",self.time)
            self.game_over=True


        self.update_snapshot()

    def update_snapshot(self):
        self.snapshot["test_field"]=self.time