import pygame

class TileSet:
    def __init__(self, image_path: str, tile_width: int, tile_height: int) -> None:
        self.image_path = image_path
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.image = None
        self.tiles = {}

    def extract_tiles(self) -> None:
        self.image = pygame.image.load(self.image_path)

        for y in range(0, tile_set.get_height(), tile_height):
            for x in range(0, tile_set.get_width(), tile_width):
                tile = tile_set.subsurface((x, y, tile_width, tile_height))
                tiles[(x // tile_width, y // tile_height)] = tile

