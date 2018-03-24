from typing import Tuple

import pygame

from fruits.game_object import GameObject


class Background(GameObject):
    def __init__(self,
                 background_image_path: str,
                 size: Tuple[int, int]
                 ) -> None:
        super(Background, self).__init__(background_image_path, (0, 0))
        self.image = pygame.transform.scale(self.image, size)

    def update(self, *args):
        pass
