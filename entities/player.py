import pygame
from entities import entity

class Player(entity.Entity):
    def draw(self) -> None:
        pygame.draw.rect(
            self.screen,
            self.color,
            (
                self.x,
                self.y,
                self.size[0] - self.padding,
                self.size[1] - self.padding,
            ),
            5,
        )

    def update(self, event: pygame.event.Event) -> None:
        self.update_count += 1
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_d:
                self.x += self.speed
            if event.key == pygame.K_a:
                self.x -= self.speed
            if event.key == pygame.K_w:
                self.y -= self.speed
            if event.key == pygame.K_s:
                self.y += self.speed
