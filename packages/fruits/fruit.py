from typing import Tuple
from fruits.game_components import Collider
import pygame

from fruits.controllers.fruit_controller import FruitController
from fruits.game_object import GameObject
import fruits.shared_preferences as shared
from fruits.game_components import Mesh


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

        self.mesh = Mesh(image=image, position=position, orientation=orientation, vx=vx, vy=vy, ax=ax, ay=ay,
                         width=shared.character_width, height=shared.character_height)

        self.collider = Collider(pygame.mask.from_surface(self.mesh.image), self.mesh.rect)

    def init(self) -> None:
        pass

    def update(self,
               horizontal: int = 0,
               vertical: int = 0,
               *args) -> None:
        if self.is_selected:
            self.mesh.vx += horizontal
            self.mesh.vy += vertical

    def move(self,
             collided: bool) -> None:
        if collided:
            self.mesh.vx = 0
            self.mesh.vy = 0
            self.mesh.position = self.mesh.last_position
        else:
            self.mesh.last_position = self.mesh.position
            self.mesh.position = ((self.mesh.position[0] + self.mesh.vx) % shared.window_width,
                             (self.mesh.position[1] + self.mesh.vy))

        self.collider.rect = self.mesh.rect
        self.collider.mask = pygame.mask.from_surface(self.mesh.image)

    def update_selected_status(self):
        if self.is_selected:
            self.is_selected = False
            self.mesh.update_image(self.mesh.image_path.replace('happy', 'sad'))
        else:
            self.is_selected = True
            self.mesh.update_image(self.mesh.image_path.replace('sad', 'happy'))
