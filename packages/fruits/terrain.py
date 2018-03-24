from typing import Tuple

import pygame

from fruits.game_object import GameObject


class Terrain(GameObject):
    def __init__(self, image: str, position: Tuple[int, int]) -> None:
        super(Terrain, self).__init__(image, position)
        self.image = self.image.copy().convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        size = self.image.get_size()

        self.position = (position[0] - .5*size[0],
                         position[1] - .5*size[1])

    def update(self, *args):
        pass
