from abc import ABC
import abc
from typing import Iterable
from random import randint
from fruits.game_object import GameObject
import fruits.background
import fruits.terrain
import fruits.fruit
import fruits.shared_preferences as shared
import pygame


class World(ABC):

    def __init__(self) -> None:
        self._drawables = []
        self.fruits = pygame.sprite.Group()
        self.current_fruit = -1

    def register(self, game_object: GameObject) -> None:
        if game_object is not None:
            self._drawables.append(game_object)
            if type(game_object) == fruits.fruit.Fruit:
                self.fruits.add(game_object)

    @property
    def drawables(self) -> Iterable[GameObject]:
        return self._drawables

    def update_current_fruit(self):
        if self.current_fruit == -1:
            self.current_fruit = randint(0, len(self.fruits) - 1)
            self.fruits.sprites()[self.current_fruit].update_selected_status()
            return

        if len(self.fruits) < 2:
            return

        i = -1
        while i != self.current_fruit:
            i = randint(0, len(self.fruits) - 1)

        self.fruits.sprites()[i].update_selected_status()
        self.fruits.sprites()[(i + 1) % len(self.fruits)].update_selected_status()
        self.current_fruit = (i + 1) % len(self.fruits)


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()

        # TODO: Create TerrainManager

        self.__terrain = fruits.terrain.Terrain('terrain.png', (0, 0))
        fruit1 = fruits.fruit.Fruit('tomato-sad.png', position=(1200, 100))
        fruit2 = fruits.fruit.Fruit('tomato-sad.png', position=(1200, 200))
        fruit3 = fruits.fruit.Fruit('tomato-sad.png', position=(1200, 300))
        fruit4 = fruits.fruit.Fruit('tomato-sad.png', position=(1200, 400))
        fruit5 = fruits.fruit.Fruit('tomato-sad.png', position=(1200, 500))
        self.register(self.__terrain)
        self.register(fruit1)
        self.register(fruit2)
        self.register(fruit3)
        self.register(fruit4)
        self.register(fruit5)

        self.update_current_fruit()

    def catch_fruits_terrain_collisions(self) -> None:
        if pygame.sprite.spritecollide(self.__terrain, self.fruits, False):
            collisions = pygame.sprite.spritecollide(self.__terrain, self.fruits, False, pygame.sprite.collide_mask)
            if collisions != []:
                for sprite_collided in collisions:
                    sprite_collided.update(collided=True)
                return True
        return False

