import os
import sys

import pygame
import requests


class Map:
    def __init__(self):
        self.pos = (68.34, 70.58)
        self.scale = 0.2

    def get_cart_picture(self):
        map_request = (
            f"http://static-maps.yandex.ru/1.x/?ll={self.pos[0]},{self.pos[1]}&spn={self.scale},{self.scale}&l=map")
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

    def draw(self, screen):
        self.get_cart_picture()
        screen.blit(pygame.image.load("map.png"), (0, 0))
