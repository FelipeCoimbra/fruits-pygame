from typing import Tuple
from fruits.game_components import Collider
import pygame

from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
from fruits.game_components import Mesh
from fruits.controllers.bomb_controller import BombController
from fruits.utils import load_image

from fruits.geometry.vector2d import Vector2D


class Bomb(GameObject):
    always_update = True

    def __init__(self,
                 position: Vector2D = None,
                 orientation: float = None,
                 velocity: Vector2D = None) -> None:
        super().__init__(GameObjectTransform(position=position, velocity=velocity,
                                             orientation=orientation))
        self.image = 'bomb-normal.png'
        self.launched = False
        self.hitted_terrain = False
        self.exploded = False

        self.frame_count = 0
        self.is_selected = False
        self.mesh = Mesh(self,
                         image=self.image,
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
        if self.should_explode() and not self.exploded:
            print('BOOOOOOOOOOM')
            self.controller.explode()
            self.exploded = True

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
        return self.launched and (self.frame_count >= 6 * 60 or self.hitted_terrain)

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
