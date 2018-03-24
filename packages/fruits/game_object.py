import abc
from typing import Tuple

import pygame

from fruits.utils import load_image


class GameObject(pygame.sprite.Sprite, abc.ABC):
    def __init__(self,
                 position: Tuple[int, int],
                 speed: float=None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.position = position
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