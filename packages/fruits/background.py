from typing import Tuple

import pygame

from fruits.game_object import GameObject, Mesh
import fruits.shared_preferences as shared


class Background(GameObject):
    def __init__(self,
                 background_image_path: str) -> None:
        super(Background, self).__init__((0, 0))

        self.mesh = Mesh(self, background_image_path)
        self.mesh.image = pygame.transform.scale(self.mesh.image, (shared.window_width,
                                                                   shared.window_height))

    def update(self, *args):
        pass

    def init(self):
        pass
