import pygame
from map import Map


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    map = Map()
    while pygame.event.wait().type != pygame.QUIT:
        map.draw(screen)
        pygame.display.flip()
    pygame.quit()
