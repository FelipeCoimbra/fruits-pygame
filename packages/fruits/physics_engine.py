from fruits.world import FruitsWorld
import pygame


class PhysicsEngine(object):
    def __init__(self,
                 world: FruitsWorld):
        self.gravity = 2
        self.friction_x = 0.6
        self.friction_y = 0.6
        self._world = world

    def move_fruits(self):
        for fruit in self._world.fruits:
            fruit.mesh.vy += self.gravity
            fruit.move(collided=False)
            if pygame.sprite.collide_mask(self._world._terrain.collider, fruit.collider) is not None:
                fruit.move(collided=True)
            else:
                fruit.mesh.vx *= self.friction_x
