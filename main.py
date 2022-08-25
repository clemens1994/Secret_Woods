import pygame, sys
from settings import *

class Game(object):
    """docstring for Game."""

    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((g_width, g_height))
        self.clock  = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(g_fps)


if __name__ == '__main__':
    game = Game()
    game.run()
