import sys

import pygame
from pygame.locals import QUIT, RESIZABLE

from entities import player
from world import grid

tile_set = pygame.image.load('./data/basictiles.png')

def main() -> None:
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 1000), RESIZABLE)
    color = (50, 50, 50)

    game_running = True

    level_grid = grid.Grid(screen, 10, 10, 50)
    current_player = player.Player(screen, level_grid)
    while game_running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            current_player.update(event)
        screen.fill(color)
        screen.blit(tile_set,(0,0))
        level_grid.draw()
        current_player.draw()

        pygame.display.update()



if __name__ == "__main__":
    main()
