import pygame
import requests


class Map:
    def __init__(self):
        self.pos = [68.34, 70.58]
        self.scale = 1

    def set_pos_x(self, value):
        self.pos[0] = value

    def get_pos_x(self):
        return self.pos[0]

    def set_pos_y(self, value):
        self.pos[1] = value

    def get_pos_y(self):
        return self.pos[1]

    def set_zoom(self, value):
        self.scale = value

    def get_zoom(self):
        return self.scale

    def get_cart_picture(self):
        map_request = (f"http://static-maps.yandex.ru/1.x/?ll={self.pos[0]},{self.pos[1]}&spn="
                       f"{0.2 * self.scale},{0.2 * self.scale}&l=map")
        response = requests.get(map_request)
        if response:
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)

    def draw(self, screen):
        self.get_cart_picture()
        screen.blit(pygame.image.load("map.png"), (0, 0))
