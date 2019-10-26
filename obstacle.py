from gameConstants import *
import random
import pygame
from colorAPI import *

obstacleImg = pygame.image.load("./resources/images/obstacle.png")
obstacleImgFlip = pygame.transform.flip(obstacleImg, False, True)
obstacleMask = pygame.mask.from_surface(obstacleImg)
obstacleMaskFlip = pygame.mask.from_surface(obstacleImgFlip)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, height, f_inverted):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.f_inverted = f_inverted
        self.x = OBS_INITX
        self.vx = OBS_VEL
        self.image = obstacleImgFlip if f_inverted else obstacleImg
        self.mask = obstacleMaskFlip if f_inverted else obstacleMask
        self.rect = self.image.get_rect()
        self.setRectPos()
        self.f_pop = False

    def setRectPos(self):
        self.rect.x, self.rect.y = int(self.x - self.rect.width/2), int((self.height - self.rect.height) if self.f_inverted else self.height)

    def update(self, deltaTime, keyStrokes, events):
        self.x += self.vx * deltaTime
        self.setRectPos()
        if self.x < -self.rect.width/2:
            self.f_pop = True

    @staticmethod
    def generatePair(height, spacing):
        # height = random.randint(0, RES[1] - spacing)
        o1 = Obstacle(height, True)
        o2 = Obstacle(height + spacing, False)
        return (o1, o2)
