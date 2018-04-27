from typing import Tuple
from fruits.game_components import Collider
from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
import pygame
from fruits.game_components import Mesh
from fruits.geometry.vector2d import Vector2D
from fruits.controllers.terrain_controller import TerrainController
from fruits.explosion_effect import ExplosionEffect


class Terrain(GameObject):
    def __init__(self, image: str,
                 position: Vector2D =Vector2D(0, 0)) -> None:
        super().__init__(GameObjectTransform(position))

        self.attach_controller(TerrainController(self))

        self.mesh = Mesh(self, image, width=shared.window_width, height=shared.window_height)
        self.collider = Collider(pygame.mask.from_surface(self.mesh.image), self.mesh.rect)

        # self.mesh.image.set_alpha()
        # self.mesh.image.set_colorkey((0,255,100))

    def init(self) -> None:
        pass

    def update(self, *args) -> None:
        pass

    def destroy(self, explosion: ExplosionEffect):
        self.mesh.image.get_masks().erase(explosion.mesh.image.get_masks())
        pass
