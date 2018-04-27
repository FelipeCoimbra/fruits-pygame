from typing import Tuple
from fruits.game_components import Collider
import pygame

from fruits.game_object import GameObject
import fruits.shared_preferences as shared
from fruits.game_components import Mesh
from fruits.controllers.bomb_controller import BombController
from fruits.utils import load_image


class Bomb(GameObject):
    always_update = True

    def __init__(self,
                 position: Tuple[int, int] = (0, 0),
                 orientation: float = None,
                 vx: float = 0,
                 vy: float = 0,
                 ax: float = 0,
                 ay: float = 0) -> None:
        super(GameObject, self).__init__()
        self.image = 'bomb-normal.png'

        self.frame_count = 0
        self.is_selected = False
        self.mesh = Mesh(image=self.image, position=position,
                         orientation=orientation, vx=vx, vy=vy, ax=ax, ay=ay,
                         width=shared.character_width,
                         height=shared.character_height)
        self.collider = Collider(pygame.mask.from_surface(self.mesh.image),
                                 self.mesh.rect)

        self.attach_controller(BombController(self))

    def init(self) -> None:
        pass

    def update(self) -> None:
        pass

    def update_frame(self) -> None:
        self.frame_count += 1
        if self.should_explode():
            print('BOOOOOOOOOOM')
            self.controller.explode()

        if (2 * 60 <= self.frame_count <= 4 * 60
                and 'normal' in self.image):
            self.last_image = 'bomb-normal.png'
            self.image = 'bomb-yellow.png'
            self.mesh.update_image(self.image)
        elif (4 * 60 < self.frame_count < 5 * 60
                and 'yellow' in self.image):
            self.last_image = 'bomb-yellow.png'
            self.image = 'bomb-red.png'
            self.mesh.update_image(self.image)

        if 2 * 60 <= self.frame_count <= 5 * 60:
            if self.frame_count % 30 in (0, 15):
                self.mesh.update_image(self.last_image)
                self.image, self.last_image = self.last_image, self.image
        elif self.frame_count > 5 * 60:
            self.mesh.update_image('bomb-red.png')

    def should_explode(self) -> bool:
        return self.frame_count >= 6 * 60

    def move(self, collided: bool) -> None:
        if collided:
            self.mesh.vx = 0
            self.mesh.vy = 0
            self.mesh.position = self.mesh.last_position
        else:
            self.mesh.last_position = self.mesh.position
            self.mesh.position = (
                (self.mesh.position[0] + self.mesh.vx + .5 * self.mesh.ax) % shared.window_width,
                (self.mesh.position[1] + self.mesh.vy + .5 * self.mesh.ay))

        self.collider.rect = self.mesh.rect
        self.collider.mask = pygame.mask.from_surface(self.mesh.image)

    def update_selected_status(self):
        pass
