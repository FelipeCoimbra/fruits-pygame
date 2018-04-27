from typing import Tuple
from fruits.game_components import Collider
from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
import pygame, math
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

        self.mesh.image.set_alpha(0)
        self.mesh.image.set_colorkey((255, 0, 255))

    def init(self) -> None:
        pass

    def update(self, *args) -> None:
        pass

    def destroy(self, explosion: ExplosionEffect):
        # terrain_mask = pygame.sprite.from_surface(self.mesh.image)
        # explosion_mask = pygame.sprite.from_surface(explosion.mesh.image)
        # terrain_mask.erase(explosion_mask, (0, 0))
        # self.mesh.mask = terrain_mask
        # pygame.draw.circle(self.mesh.image, (255, 0, 255, 0),(math.floor(explosion.position.x+40), math.floor(explosion.position.y+40)), 40)
        pass
