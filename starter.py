
import pygame
from pygame.locals import *
from pygamehelper import *
from vec2d import *

class Game(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h))

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()

g = Game()
g.mainLoop(60)
