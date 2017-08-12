import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = self.image.get_rect()
        self.selected = False
        self.name='player'
        self.loc = [0,0]


    def update(self):
        pass