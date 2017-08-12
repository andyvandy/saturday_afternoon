"""
This file houses the game menu. Bassically, it diverts the game loop to the game menu loop until the Start button is chosen
which then activates the start_game fucntion, routing the game loop to the actual game loop. 
"""
from main import Game
import pygame as pg
import sys
try:
    from settings import *
except ModuleNotFoundError:
    from .settings import *

class GameMenu():
    def __init__(self, game, bg_color=WHITE, font=None, font_size=MENU_FONTSIZE, font_color=BLACK, items=MENU_ITEMS):
        self.game = game
        self.menu = True
        self.bg_color = bg_color
        self.clock = self.game.clock
        self.screen = self.game.screen
        #font options
        self.font = pg.font.SysFont(font, font_size)
        self.font_color = MENU_FONTCOLOUR
        self.items = []
        for item in items:
            label = self.font.render(item, 1, font_color)
            self.items.append(label)

    def start_game(self):
        print("Starting game")
        return

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed
            self.clock.tick(FPS)
 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    mainloop = False
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mpos = pg.mouse.get_pos()
                    print(mpos)
                    if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 465 and mpos[1] < 495:
                        mainloop = False
                        self.start_game()
                    if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 565 and mpos[1] < 595:
                        print("Exiting Game")
                        self.quit()

                        
 
            # Redraw the background
            self.game.screen.fill(self.bg_color)

            for index, label in enumerate(self.items):
                if index == 0:
                    #Title
                    self.screen.blit(label, (300, 262))
                if index == 1:
                    #Start
                    self.screen.blit(label, (445, 462))
                if index == 2:
                    #Quit
                    self.screen.blit(label, (445, 562))

            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()
