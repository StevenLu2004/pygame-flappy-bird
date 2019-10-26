from gameConstants import *
import math
import pygame
from colorAPI import *

birdImg = pygame.image.load("./resources/images/bird.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        pygame.sprite.Sprite.__init__(self)
        self.cy, self.cx = cy, cx
        self.vy = 0
        self.ay = BIRD_ACCEL
        self.baseImage = birdImg
        self.prevAngle = None
        self.initImgs()
        self.updateImg()
        self.jump = BIRD_JUMP
        self.f_jumping = False

    def setRectPos(self):
        self.rect.y, self.rect.x = int(self.cy - self.rect.height / 2), int(self.cx - self.rect.width / 2)

    def initImgs(self):
        self.images = {angle: pygame.transform.rotate(self.baseImage, -angle) for angle in range(-180, 180)}
        self.rects = {angle: self.images[angle].get_rect() for angle in range(-180, 180)}
        self.masks = {angle: pygame.mask.from_surface(self.images[angle]) for angle in range(-180, 180)}

    def updateImg(self):
        angle = int(math.atan(self.vy / BIRD_ANGLE_CONSTANT) * 180 / math.pi)  # TODO: game speed constant
        if angle != self.prevAngle:
            self.image = self.images[angle]
            self.mask = self.masks[angle]
            self.rect = self.rects[angle].copy()
        self.setRectPos()
        self.prevAngle = angle

    def update(self, deltaTime, keyStrokes, events):
        self.cy += self.vy * deltaTime
        self.vy += self.ay * deltaTime
        if keyStrokes[pygame.K_SPACE] and (not self.f_jumping):
            self.vy += self.jump
            if self.vy < BIRD_MINVEL:
                self.vy = BIRD_MINVEL
            self.f_jumping = True
        elif (not keyStrokes[pygame.K_SPACE]) and self.f_jumping:
            self.f_jumping = False
        self.updateImg()
