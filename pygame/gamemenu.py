import pygame as pg
from settings import *

class GameMenu():
    def __init__(self, bg_color=WHITE, font=None, font_size=MENU_FONTSIZE, font_color=BLACK):
        pg.init()
        self.menu = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bg_color = bg_color
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        #font options
        self.font = pg.font.SysFont(font, font_size)
        self.font_color = MENU_FONTCOLOUR
        self.items = []
        for item in self.items:
            label = self.font.render(item, 1, font_color)
            self.items.append(label)

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(FPS)
 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)

            for label in self.items:
                self.screen.blit(label, (100, 100))

            pg.display.flip()
 