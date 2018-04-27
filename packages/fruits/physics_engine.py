from fruits.world import FruitsWorld
from fruits.fruit import Fruit
from fruits.geometry.vector2d import Vector2D
import fruits.shared_preferences as shared
from fruits.game_object import GameObject
from fruits.game_components import Collider
import pygame
import math, copy


class PhysicsEngine(object):
    def __init__(self,
                 world: FruitsWorld):
        self.gravity = 10
        self.friction_x = 0.5
        self.friction_y = 0.6
        self._world = world

    def __move(self, game_object: Fruit) -> None:
        game_object.position = Vector2D((game_object.position.x + game_object.velocity.x) % shared.window_width,
                                  (game_object.position.y + game_object.velocity.y))

        game_object.update_components()
        if game_object.collider is not None and game_object.mesh is not None:
            game_object.collider.mask = pygame.mask.from_surface(game_object.mesh.image)

    def __handle_terrain_collision(self, game_object: GameObject):
        if game_object.collider is not None and game_object.collider.enabled:
            collision_tuple = pygame.sprite.collide_mask(self._world.terrain.collider, game_object.collider)
            if collision_tuple is not None:
                # First bring the object to the contact point
                translation_vector = game_object.position - game_object.last_position
                translation_vector -= self.__binary_search_static_collision(translation_vector, game_object,
                                                                           self._world.terrain.collider)
                while True:
                    game_object.position = game_object.last_position + translation_vector

                # Then add an impulse depending on the collision elasticity
                collision_point = Vector2D.from_cardinal_tuple(collision_tuple)

    def __binary_search_static_collision(self, total_translation: Vector2D, moving_obj: GameObject,
                                         static_collider: Collider) -> Vector2D:
        trie_vector = copy.deepcopy(total_translation)
        initial_position = copy.deepcopy(moving_obj.position)

        max_translation = total_translation.r
        min_translation = 0
        eps = 0.0001
        while math.fabs(max_translation-min_translation) > eps:
            mid_tranlation = (min_translation + max_translation)/2.0
            trie_vector = Vector2D.from_polar(r=mid_tranlation, ang=total_translation.ang)
            moving_obj.position -= trie_vector

            if pygame.sprite.collide_mask(static_collider, moving_obj.collider):
                min_translation = mid_tranlation
            else:
                max_translation = mid_tranlation

            moving_obj.position = initial_position
        # if moving_obj.is_selected:
            # print(trie_vector.x, trie_vector.y)
        return 1.01*trie_vector

    def apply_user_commands(self) -> None:
        for fruit in self._world.fruits:
            self.__handle_terrain_collision(fruit)
            self.__move(fruit)
            # fruit.velocity.x *= self.friction_x

    def apply_fields(self):
        for fruit in self._world.fruits:
            fruit.velocity.y += self.gravity
            self.__handle_terrain_collision(fruit)
            self.__move(fruit)

    def apply_destruction(self):
        pass

    def flush(self):
        for fruit in self._world.fruits:
            fruit.flush_transform()

