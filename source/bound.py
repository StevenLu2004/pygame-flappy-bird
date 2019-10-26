from gameConstants import *
import pygame
from colorAPI import *

boundImg = pygame.image.load("./resources/images/bound.png")
boundRect = boundImg.get_rect()
boundMask = pygame.mask.from_surface(boundImg)

class Bound(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = boundImg
        self.mask = boundMask
        self.rect = boundRect.copy()
        self.rect.x, self.rect.y = pos[0], pos[1]

    def update(self, deltaTime, keyStrokes, events):
        pass

    @staticmethod
    def getUpperLowerBounds():
        ub = Bound((0, -boundRect.height))
        lb = Bound((0, RES[1]))
        return (ub, lb)
