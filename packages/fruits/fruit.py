from typing import Tuple

import pygame

from fruits.controllers.fruit_controller import FruitController
from fruits.game_object import GameObject
import fruits.shared_preferences as shared


class Fruit(GameObject):
    def __init__(self,
                 image: str,
                 position: Tuple[int, int] = (0,0),
                 orientation: float = None,
                 speed: float = None) -> None:
        super(GameObject, self).__init__()
        self.attach_controller(FruitController(self))
        self.set_component("Mesh", image=image, position=position, orientation=orientation, speed=speed)
        self.set_component("Collider")

        self.image = pygame.transform.scale(self.image, (shared.character_width, shared.character_height))

    def init(self) -> None:
        pass

    def update(self, horizontal=0, vertical=0, *args):
        self.position = (self.position[0] + horizontal, self.position[1] + vertical)

