import pygame as pg
try:
    from settings import *
except ModuleNotFoundError:
    from .settings import *

class Camera:
    def __init__(self,width,height):
        self.x = 0
        self.y = 0
        self.camera = pg.Rect(self.x, self.y, width, height)
        self.width = width
        self.height = height
        self.cameraposx = WIDTH/2
        self.cameraposy = HEIGHT/2

    def update(self):
        self.camera = pg.Rect(self.x,self.y,self.width,self.height)
