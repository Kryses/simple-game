import pygame



class GridCell:
    def __init__(self, index: int, x: int, y: int):
        self.index = index
        self.x = x
        self.y = y
        self.midpoint = ((x + 1) / 2, (y + 1) / 2)
        self.entities: list['entities.Entity'] = []

    def add_entity(self, current_entity: 'entities.Entity') -> None:
        self.entities.append(current_entity)

    def remove_entity(self, current_entity: 'entities.Entity') -> None:
        self.entities.remove(current_entity)

    def __repr__(self) -> str:
        return f"Cell: x:{self.x} y:{self.y}"

class Grid:
    def __init__(
        self,
        screen: pygame.Surface,
        grid_rows: int,
        grid_columns: int,
        grid_spacing: int,
    ) -> None:
        self.screen = screen
        self.grid_rows = grid_rows
        self.grid_columns = grid_columns
        self.grid_spacing = grid_spacing
        self.cells = []

        index = 0
        for x in range(0, self.grid_columns):
            for y in range(0, self.grid_rows):
                self.cells.append(GridCell(index, x, y))
                index += 1

    def get_cell(self, position: tuple[int, int]) -> GridCell:
        for cell in self.cells:
            if cell.x == position[0] and cell.y == position[1]:
                return cell
        raise ValueError(f"Unable to find cell at {position}")

    def draw(self) -> None:
        for row in range(self.grid_rows):
            for col in range(self.grid_columns):
                pygame.draw.rect(
                    self.screen,
                    (100, 100, 100),
                    (col * self.grid_spacing, row * self.grid_spacing,
                    self.grid_spacing,
                    self.grid_spacing),
                    1,
                )

