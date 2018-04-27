from fruits.world import FruitsWorld
from fruits.fruit import Fruit
from fruits.geometry.vector2d import Vector2D
import fruits.shared_preferences as shared
from fruits.game_object import GameObject
from fruits.game_components import Collider
import pygame
from fruits.bomb import Bomb
import math, copy


class PhysicsEngine(object):
    def __init__(self,
                 world: FruitsWorld):
        self.gravity = 1
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
                offset = game_object.position-game_object.last_position
                game_object.position = game_object.last_position
                if offset.r < 5:
                    game_object.velocity = Vector2D(0, 0)
                    game_object.jumping = False
                    game_object.walking = False
                else:
                    game_object.velocity *= 1/offset.r
                if isinstance(game_object, Bomb) and game_object.frame_count > 30:
                    game_object.hitted_terrain = True
                # game_object.position = game_object.last_position
                # collision_pos = Vector2D.from_cardinal_tuple(collision_tuple)
                # collision_dir = collision_pos - game_object.position
                # collision_dir.r = 1
                # perp_vel = Vector2D(collision_dir.x, collision_pos.y)
                # if game_object.velocity.x > 0:
                #     perp_vel.ang -= math.pi / 2
                # else:
                #     perp_vel.ang += math.pi / 2
                # perp_vel.r = perp_vel.r*math.sin(collision_dir.ang - game_object.velocity.ang)
                # game_object.velocity = perp_vel
                # return
                # First bring the object to the contact point
                # translation_vector = game_object.position - game_object.last_position
                # translation_vector -= self.__binary_search_static_collision(translation_vector, game_object,
                #                                                            self._world.terrain.collider)

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

        for drawable in self._world.drawables:
            if hasattr(drawable, 'always_update'):
                drawable.update_frame()

            if isinstance(drawable, Bomb):
                drawable.mesh.vy += self.gravity
                drawable.move(collided=False)
                if pygame.sprite.collide_mask(self._world._terrain.collider, 
                                              drawable.collider) is not None:
                    drawable.move(collided=True)
                else:
                    drawable.mesh.vx *= self.friction_x

            moving_obj.position = initial_position
        # if moving_obj.is_selected:
            # print(trie_vector.x, trie_vector.y)
        return 1.01*trie_vector

    def apply_user_commands(self) -> None:
        for fruit in self._world.fruits:
            self.__move(fruit)
            self.__handle_terrain_collision(fruit)
            self.flush_fruits()
            # fruit.velocity.x *= self.friction_x

    def apply_fields(self):
        if self._world.bomb is not None and self._world.bomb.launched:
            self._world.bomb.velocity.y += self.gravity
            self.__move(self._world.bomb)
            self.__handle_terrain_collision(self._world.bomb)
            self._world.bomb.flush_transform()
        for fruit in self._world.fruits:
            fruit.velocity.y += self.gravity
            self.__move(fruit)
            self.__handle_terrain_collision(fruit)
            self.flush_fruits()

    def apply_destruction(self):
        pass

    def flush_fruits(self):
        for fruit in self._world.fruits:
            fruit.flush_transform()

    def negate(self):
        for fruit in self._world.fruits:
            fruit.position = fruit.last_position
            fruit.velocity = fruit.last_velocity

