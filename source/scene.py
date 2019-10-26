import pygame
from colorAPI import *

class Scene(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.lastActiveScene = None
        self.activeScene = None
        self.nextActiveScene = None

    def update(self, deltaTime, keyStrokes, events, activeScene):
        for sprite in self.sprites():
            sprite.update(deltaTime, keyStrokes, events)

    def getNextActiveScene(self):
        return self.nextActiveScene
