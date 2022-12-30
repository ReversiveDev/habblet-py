import pygame

def project(x, y, z):
    return (x - y, x * 0.5 + y * 0.5 - z)

class Tile:
    def __init__(self, roomX, roomY, roomZ):
        self.roomX = roomX
        self.roomY = roomY
        self.roomZ = roomZ
        self.x = 0
        self.y = 0
        self._update_position()

    def _update_position(self):
        (self.x, self.y) = project(self.roomX * 32, self.roomY * 32, self.roomZ * 32)

    def get_position(self):
        return (self.x, self.y)

class Room:
    def __init__(self, screen):
        self.screen = screen
        self.x = 600
        self.y = 300
        self.tile_texture = pygame.image.load("room/tile.png").convert_alpha()
        self.tiles = []
        self.width = 5
        self.heigth = 5
        for i in range(self.width * self.heigth):
            x = i % self.width
            y = int(i / self.width)
            self.tiles.append(Tile(x, y, 0))
    def render(self):
        for tile in self.tiles:
            (x, y) = tile.get_position()
            self.screen.blit(self.tile_texture, (x + self.x, y + self.y))
    def get_tile_by_point(self, px, py):
        rect = self.tile_texture.get_rect()
        for tile in self.tiles:
            (x, y) = tile.get_position()
            rect.x = x + self.x
            rect.y = y + self.y
            difx = px - rect.x
            dify = py - rect.y
            if rect.collidepoint(px, py) and self.tile_texture.get_at((difx, dify)).a > 0:
                return tile
        return None