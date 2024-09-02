import pygame
import uuid
from world import grid

class Entity:
    speed = 1
    def __init__(self, screen: pygame.Surface, level_grid: grid.Grid, spawn_location: tuple[int, int] = (0, 0)) -> None:
        self.uuid = uuid.uuid4()
        self.update_count = 0
        self.level_grid = level_grid
        self.x: int = spawn_location[0]
        self.y: int = spawn_location[1]
        self.screen: pygame.surface.Surface = screen
        self.color: tuple[int, int, int] = (100, 100, 255)
        self.size: tuple[int, int] = (50, 50)
        self.padding = 10
        self.move_speed = self.speed * self.level_grid.grid_spacing

        self.cell = self.level_grid.get_cell(self.current_position)
        self.cell.add_entity(self)


    def move(self, new_position: tuple[int, int]) -> None:
        if self.cell:
            self.cell.remove_entity(self)

        new_pos_x, new_pos_y = new_position

        if new_pos_x > self.level_grid.grid_columns - 1 or new_pos_x < 0:
            new_pos_x = self.x
        if new_pos_y > self.level_grid.grid_rows - 1 or new_pos_y < 0:
            new_pos_y = self.y

        new_position = (new_pos_x, new_pos_y)

        next_cell = self.level_grid.get_cell(new_position)
        next_cell.add_entity(self)
        self.x = next_cell.x
        self.y = next_cell.y
        self.cell = next_cell
        print(self.cell)

    @property
    def current_position(self) -> tuple[int, int]:
        return (self.x, self.y)
