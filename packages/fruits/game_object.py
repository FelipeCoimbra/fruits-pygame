import abc
from typing import Tuple

import pygame

from fruits.utils import load_image
from fruits.game_entity import GameEntity


class GameObject(GameEntity, abc.ABC):
    def __init__(self,
                 position: Tuple[int, int]=None,
                 orientation: float=None,
                 speed: float=None) -> None:
        GameEntity.__init__(self)

        self.position = position
        self.orientation = orientation
        self.speed = speed

        self.mesh = None
        self.collider = None
        self.rigid_body = None

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def update(self, *args):
        pass


class Mesh(abc.ABC):

    def __init__(self,
                 object: GameObject,
                 image: str):
        self.__object = object
        self.image = self.image = load_image(image)
        self.rect = self.image.get_rect()

    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()

    def draw_on(self, screen) -> None:
        screen.blit(self.image, self.__object.position)


class Collider(pygame.sprite.Sprite, abc.ABC):

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)


class RigidBody(abc.ABC):

    def __init__(self, mass: float=None) -> None:
        self.mass = mass
