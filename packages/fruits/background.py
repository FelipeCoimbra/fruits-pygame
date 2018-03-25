from typing import Tuple

import pygame

from fruits.game_object import GameObject
import fruits.shared_preferences as shared


class Background(GameObject):
    def __init__(self,
                 background_image_path: str) -> None:
        self.set_component("Mesh", image=background_image_path, position=(0, 0))

        self.image = pygame.transform.scale(self.image, (shared.window_width,
                                                                   shared.window_height))

    def update(self, *args):
        pass

    def init(self):
        pass
