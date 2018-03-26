from typing import Tuple

import pygame

from fruits.game_object import GameObject


class Terrain(GameObject):
    def __init__(self, image: str, position: Tuple[int, int]) -> None:
        super(GameObject, self).__init__()

        self.set_component("Mesh", image=image, position=position)
        self.set_component("Collider")

        self.image = pygame.transform.scale2x(self.image)

        size = self.image.get_size()

        self.position = (position[0] - .5*size[0],
                         position[1] - .5*size[1])

        self.rect = self.image.get_rect()
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
        self.mask = pygame.mask.from_surface(self.image)

    def init(self) -> None:
        pass

    def update(self, *args) -> None:
        self.mask = pygame.mask.from_surface(self.image)
        pass
