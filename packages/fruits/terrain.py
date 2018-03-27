from typing import Tuple

import pygame

from fruits.game_object import GameObject
import fruits.shared_preferences as shared


class Terrain(GameObject):
    def __init__(self, image: str,
                 position: Tuple[int, int]) -> None:
        super(GameObject, self).__init__()

        self.set_component("Mesh", image=image, position=position, width=shared.window_width,
                           height=shared.window_height)

    def init(self) -> None:
        pass

    def update(self, *args) -> None:
        self.mask = pygame.mask.from_surface(self.image)
        pass
