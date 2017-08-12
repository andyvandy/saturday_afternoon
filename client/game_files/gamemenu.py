"""
This file houses the game menu. Bassically, it diverts the game loop to the game menu loop until the Start button is chosen
which then activates the start_game fucntion, routing the game loop to the actual game loop. 
"""

import pygame as pg
import sys
try:
    from settings import *
except ModuleNotFoundError:
    from .settings import *

class GameMenu():
    def __init__(self, game, bg_color=WHITE, font=None, font_size=MENU_FONTSIZE, font_color=BLACK, menuitems=MENU_ITEMS):
        self.font_color = font_color
        self.menuitems = menuitems
        self.game = game
        self.menu = True
        self.bg_color = bg_color
        self.menubg = bg = pg.image.load("assets/bg.png")
        self.clock = self.game.clock
        self.screen = self.game.screen
        #font options
        self.font = pg.font.SysFont(font, font_size)
        self.font_color = MENU_FONTCOLOUR
        self.items = []
        for item in menuitems:
            label = self.font.render(item, 1, font_color)
            self.items.append(label)

    def start_game(self):
        print("Starting game")
        return

    def run(self):
        mainloop = True
        start_hover = False
        quit_hover = False
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
                # If over menu items highlight in white
                mpos = pg.mouse.get_pos()
                if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 465 and mpos[1] < 495:
                    start_hover = True
                else:
                    start_hover = False
                if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 565 and mpos[1] < 595:
                    quit_hover = True
                else:
                    quit_hover = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mpos = pg.mouse.get_pos()
                    print(mpos)
                    if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 465 and mpos[1] < 495:
                        mainloop = False
                        self.start_game()
                    if mpos[0] > 445 and mpos[0] < 545 and mpos[1] > 565 and mpos[1] < 595:
                        print("Exiting Game")
                        self.quit()

            self.items = []
            for index, item in enumerate(self.menuitems):
                if index == 0:
                    label = self.font.render(item, 1, self.font_color)
                    self.items.append(label)
                if index == 1:
                    if start_hover == False:
                        label = self.font.render(item, 1, self.font_color)
                        self.items.append(label)
                    else:
                        label = self.font.render(item, 1, WHITE)
                        self.items.append(label)
                if index == 2:
                    if quit_hover == False:
                        label = self.font.render(item, 1, self.font_color)
                        self.items.append(label)
                    else:
                        label = self.font.render(item, 1, WHITE)
                        self.items.append(label)
 
            # Redraw the background
            self.screen.fill(self.bg_color)
            self.screen.blit(self.menubg, (0, 0))

            for index, label in enumerate(self.items):
                if index == 0:
                    #Title
                    self.screen.blit(label, (300, 262))
                if index == 1:
                    self.screen.blit(label, (445, 462))
                if index == 2:
                    self.screen.blit(label, (445, 562))
            
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()
