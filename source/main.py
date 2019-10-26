from gameConstants import *
import pygame
from colorAPI import *
from bird import Bird
from scene import Scene
from gameScene import GameScene

def main():
    # Initialize PyGame
    pygame.init()
    win = pygame.display.set_mode(RES)
    pygame.display.set_caption("Flappy Monochrome")

    # Create Scenes
    game = GameScene()
    pause = Scene()  # TODO: PauseScene
    menu = Scene()  # TODO: MenuScene
    score = Scene()  # TODO: ScoreScene
    askQuit = Scene()  # TODO: AskQuitScene
    scenes = {"game": game, "pause": pause, "menu": menu, "score": score, "askQuit": askQuit}
    activeScene = "game"

    run = 1
    clock = pygame.time.Clock()
    ret = 0
    while run:
        clock.tick_busy_loop(FPS)
        deltaTime = clock.get_time()
        # print(clock.get_rawtime())

        events = pygame.event.get()
        keyStrokes = pygame.key.get_pressed()

        for key in scenes:
            scenes[key].update(0 if run == 1 else deltaTime, keyStrokes, events, activeScene)

        activeScene = scenes[activeScene].getNextActiveScene()
        if activeScene == "quit":
            break

        win.fill(rgb("#fff"))
        for key in scenes:
            scenes[key].draw(win)
        pygame.display.flip()

        if run == 1:
            run = 2

    pygame.quit()
    return ret

if __name__ == "__main__":
    exit(main())
