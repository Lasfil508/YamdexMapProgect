import pygame
from map import Map


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    map = Map()
    running = True
    move = {'left': False, 'right': False, 'down': False, 'up': False}
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    map.set_zoom(map.get_zoom() - 0.125)
                if event.button == 5:
                    map.set_zoom(map.get_zoom() + 0.125)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move['left'] = True
                if event.key == pygame.K_RIGHT:
                    move['right'] = True
                if event.key == pygame.K_DOWN:
                    move['down'] = True
                if event.key == pygame.K_UP:
                    move['up'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move['left'] = False
                if event.key == pygame.K_RIGHT:
                    move['right'] = False
                if event.key == pygame.K_DOWN:
                    move['down'] = False
                if event.key == pygame.K_UP:
                    move['up'] = False
        if move['left']:
            map.set_pos_x(map.get_pos_x() - 0.02)
        if move['right']:
            map.set_pos_x(map.get_pos_x() + 0.02)
        if move['down']:
            map.set_pos_y(map.get_pos_y() - 0.0075)
        if move['up']:
            map.set_pos_y(map.get_pos_y() + 0.0075)
        map.draw(screen)
        pygame.display.flip()
    pygame.quit()
