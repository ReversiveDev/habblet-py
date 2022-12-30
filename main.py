import pygame
import math
from room import Room

pygame.init()

swidth = 1280
sheight = 720
screen = pygame.display.set_mode((swidth, sheight))

room = Room(screen)

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            tile = room.get_tile_by_point(x, y)
            if not tile == None:
                continue

    # Do logical updates here.
    # ...

    screen.fill("black") # Fill the display with a solid color

    # Render the graphics here.
    room.render()

    pygame.display.flip() # Refresh on-screen display
    clock.tick(60) # wait until next frame (at 60 FPS)
    pygame.display.set_caption(f'Habblet - FPS: {str(int(clock.get_fps()))}')

