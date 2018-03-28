from typing import Tuple
from fruits.game_components import Collider
from fruits.game_object import GameObject
import fruits.shared_preferences as shared
import pygame
from fruits.game_components import Mesh


class Terrain(GameObject):
    def __init__(self, image: str,
                 position: Tuple[int, int]) -> None:
        super(GameObject, self).__init__()

        self.mesh = Mesh(image=image, position=position, width=shared.window_width, height=shared.window_height)
        self.collider = Collider(pygame.mask.from_surface(self.mesh.image), self.mesh.rect)

    def init(self) -> None:
        pass

    def update(self, *args) -> None:
        pass
