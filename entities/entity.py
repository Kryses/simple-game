import pygame
from world import grid

class Entity:
    def __init__(self, screen: pygame.Surface, level_grid: grid.Grid) -> None:
        self.update_count = 0
        self.x: float = 0.0
        self.y: float = 0.0
        self.screen: pygame.surface.Surface = screen
        self.color: tuple[int, int, int] = (100, 100, 255)
        self.size: tuple[int, int] = (50, 50)
        self.padding = 10
        self.speed = 50
        screen_size = self.screen.get_size()

        self.x = (screen_size[0] / 2) - (self.size[0] / 2) + (self.padding / 2)
        self.y = (screen_size[1] / 2) - (self.size[1] / 2) + (self.padding / 2)
