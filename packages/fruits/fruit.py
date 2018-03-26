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

        self.is_selected = False
        self.attach_controller(FruitController(self))
        self.set_component("Mesh", image=image, position=position, orientation=orientation, speed=speed)
        self.set_component("Collider")
        self.image = pygame.transform.scale(self.image, (shared.character_width, shared.character_height))

        self.last_movement = {'horizontal': 0, 'vertical': 0}

    def init(self) -> None:
        pass

    def update(self,
               horizontal: int = 0,
               vertical: int = 0,
               collided: bool = False,
               physics_engine: bool = False,
               *args):
        if self.is_selected or physics_engine:
            if not collided:
                self.last_movement = {'horizontal': -horizontal, 'vertical': -vertical}
            else:
                horizontal = self.last_movement['horizontal']
                vertical = self.last_movement['vertical']

            self.position = ((self.position[0] + horizontal) % shared.window_width,
                             (self.position[1] + vertical) % shared.window_height)
            self.rect.centerx = self.position[0]
            self.rect.centery = self.position[1]
            self.mask = pygame.mask.from_surface(self.image)

    def update_selected_status(self):
        if self.is_selected:
            self.is_selected = False
            self.update_image(self.image_path.replace('happy', 'sad'))
        else:
            self.is_selected = True
            self.update_image(self.image_path.replace('sad', 'happy'))
