import pygame as pg
import sys
try:
    from settings import *
    from sprites import *
    from camera import *
    from gamemenu import *
except ModuleNotFoundError:
    from .settings import *
    from .sprites import *
    from .camera import *
    from .gamemenu import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.game_events=[]
        self.world={"time":0}
        self.setup_rendering(font_size=MENU_FONTSIZE)

    def start (self):
        gm = GameMenu(game=self)
        gm.run()
        while True:
            self.new()
            self.run()
            self.show_go_screen()

    def load_data(self):
        pass

    def setup_rendering(self,font=None,font_size=MENU_FONTSIZE):
        self.font = pg.font.SysFont(font, font_size)
        self.font_color = MENU_FONTCOLOUR
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.camera = Camera(WIDTH,HEIGHT)
    
    def run(self):
        # game loop - set self.playing = False to end the game
        print("running game")
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.send_test_event()
        self.all_sprites.update()
        self.camera.update()

    def draw(self):
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.test_draw()
        pg.display.flip()
        

    def test_draw(self):
        print("drawing test", self.world["time"])
        label = self.font.render("server time is:" +str(self.world["time"]), 1, self.font_color)
        self.screen.blit(label, (300, 262))

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
    def send_test_event(self):
        self.game_events.append({"test":32323})
    def update_world_state(self,state):
        self.world=state

    def show_go_screen(self):
        pass

# Create the Game Menu object that will call upon the game.

# Create the Game Object
if __name__ == "__main__": # only run the game if the file is called directly

    print("switched")
    #while gm.menu == True:
    #    gm.run()
    g = Game()
    print("start")
    g.start()
    while True:
        g.new()
        g.run()
        g.show_go_screen()#