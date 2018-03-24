from typing import Tuple

import pygame

from fruits.game_object import GameObject, Mesh


class Terrain(GameObject):
    def __init__(self, image: str, position: Tuple[int, int]) -> None:
        super(Terrain, self).__init__(position)
        self.mesh = Mesh(self, image)

        self.mesh.image = pygame.transform.scale2x(self.mesh.image)

        size = self.mesh.image.get_size()

        self.position = (position[0] - .5*size[0],
                         position[1] - .5*size[1])

    def init(self) -> None:
        pass

    def update(self, *args):
        pass
