from gameConstants import *
import random
import pygame
from colorAPI import *
from scene import Scene
from bird import Bird
from obstacle import Obstacle
from bound import Bound
from timeit import default_timer as timer

obsGenModes = {"single": 0.8, "tri-tunnel": 0.18, "penta-tunnel": 0.02}

def randMode():
    m = random.random()
    for key in obsGenModes:
        if m < obsGenModes[key]:
            return key
        m -= obsGenModes[key]
    return "single"

class GameScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.bird = Bird(*BIRD_INITPOS)
        self.bounds = Bound.getUpperLowerBounds()
        # TODO: background image
        self.obstacles = []
        self.add(self.bird)
        self.add(self.bounds[0])
        self.add(self.bounds[1])
        self.plannedObsGen = []

    def reset(self):
        # Kill everything alive
        self.bird.kill()
        for o in self.obstacles:
            o.kill()
        # Recreate
        self.bird = Bird(*BIRD_INITPOS)
        self.obstacles = []  # list of obstacles
        self.add(self.bird)

    def genObs(self, t):
        mode = randMode()
        if mode == "single":
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING, "height": random.randint(0, RES[1] - OBS_SPACING), "spacing": OBS_SPACING})
        elif mode == "tri-tunnel":
            height = random.randint(0, RES[1] - OBS_SPACING)
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 1, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 2, "height": height, "spacing": OBS_SPACING})
        elif mode == "penta-tunnel":
            height = random.randint(0, RES[1] - OBS_SPACING)
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 1, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 2, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 3, "height": height, "spacing": OBS_SPACING})
            self.plannedObsGen.append({"time": t + OBS_GEN_TIMESPACING + 4, "height": height, "spacing": OBS_SPACING})

    def update(self, deltaTime, keyStrokes, events, activeScene):
        self.activeScene = activeScene
        self.nextActiveScene = "game"
        for e in events:
            if e.type == pygame.QUIT:
                self.nextActiveScene = "quit"
        if self.activeScene == "game":
            Scene.update(self, deltaTime, keyStrokes, events, activeScene)
            t = timer()
            if len(self.plannedObsGen) == 0:
                self.genObs(t)
            while len(self.plannedObsGen) and self.plannedObsGen[0]["time"] <= t:
                obs = Obstacle.generatePair(self.plannedObsGen[0]["height"], self.plannedObsGen[0]["spacing"])
                self.obstacles.extend(obs)
                self.add(obs[0])
                self.add(obs[1])
                del self.plannedObsGen[0]
            for o in self.obstacles:
                if o.f_pop:
                    o.kill()
                    self.obstacles.remove(o)
                if pygame.sprite.collide_mask(self.bird, o):
                    self.nextActiveScene = "quit"
            if pygame.sprite.collide_mask(self.bird, self.bounds[0]) or pygame.sprite.collide_mask(self.bird, self.bounds[1]):
                self.nextActiveScene = "quit"
        self.lastActiveScene = self.activeScene
