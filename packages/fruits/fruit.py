from typing import Tuple

import pygame

from fruits.controllers.fruit_controller import FruitController
from fruits.game_object import GameObject
import fruits.shared_preferences as shared


class Fruit(GameObject):
    def __init__(self,
                 image: str,
                 position: Tuple[int, int] = (0, 0),
                 orientation: float = None,
                 vx: float = 0,
                 vy: float = 0,
                 ax: float = 0,
                 ay: float = 0) -> None:
        super(GameObject, self).__init__()

        self.is_selected = False

        self.attach_controller(FruitController(self))

        self.set_component("Mesh", image=image, position=position, orientation=orientation, vx=vx, vy=vy, ax=ax, ay=ay,
                           width=shared.character_width,height=shared.character_height)

        self.last_position = self.position

    def init(self) -> None:
        pass

    def update(self,
               horizontal: int = 0,
               vertical: int = 0,
               *args) -> None:
        if self.is_selected:
            self.vx += horizontal
            self.vy += vertical

    def move(self,
             collidded: bool) -> None:
        if collidded:
            self.vx = 0
            self.vy = 0
            self.position = self.last_position
        else:
            self.last_position = self.position
            self.position = ((self.position[0] + self.vx) % shared.window_width,
                             (self.position[1] + self.vy))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.mask = pygame.mask.from_surface(self.image)

    def update_selected_status(self):
        if self.is_selected:
            self.is_selected = False
            self.update_image(self.image_path.replace('happy', 'sad'))
        else:
            self.is_selected = True
            self.update_image(self.image_path.replace('sad', 'happy'))
