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

    def init(self) -> None:
        pass

    def update(self, horizontal=0, vertical=0, *args):
        if self.is_selected:
            self.position = ((self.position[0] + horizontal) % shared.window_width,
                             (self.position[1] + vertical) % shared.window_height)
            self.rect.centerx = (self.rect.centerx + horizontal) % shared.window_width
            self.rect.centery = (self.rect.centery + vertical) % shared.window_height
            self.mask = pygame.mask.from_surface(self.image)

    def update_selected_status(self):
        if self.is_selected:
            self.is_selected = False
            self.update_image(self.image_path.replace('happy', 'sad'))
        else:
            self.is_selected = True
            self.update_image(self.image_path.replace('sad', 'happy'))
