import pygame

from entities import Entity


class Player(Entity):
    def draw(self) -> None:
        pygame.draw.rect(
            self.screen,
            self.color,
            (
                self.x * self.level_grid.grid_spacing,
                self.y * self.level_grid.grid_spacing,
                self.size[0],
                self.size[1],
            ),
            5,
        )

    def update(self, event: pygame.event.Event) -> None:
        self.update_count += 1
        if event.type in [pygame.KEYDOWN]:
            new_x = self.x
            new_y = self.y

            if event.key == pygame.K_d:
                new_x += 1
            if event.key == pygame.K_a:
                new_x -= 1
            if event.key == pygame.K_w:
                new_y -= 1
            if event.key == pygame.K_s:
                new_y += 1

            self.move((new_x, new_y))
