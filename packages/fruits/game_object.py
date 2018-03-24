import abc
from typing import Tuple

import pygame

from fruits.utils import load_image


class GameObject(pygame.sprite.Sprite, abc.ABC):
    def __init__(self,
                 image: str,
                 position: Tuple[int, int],
                 speed: float=None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.are = pygame.display.get_surface().get_rect()

        self.position = position
        self.speed = speed

    def draw_on(self, screen) -> None:
        screen.blit(self.image, self.position)

    @abc.abstractmethod
    def update(self, *args):
        pass

    @property
    def position(self) -> Tuple[int, int]:
        return self.rect.center

    @position.setter
    def position(self, position: Tuple[int, int]) -> None:
        self.rect.center = position

    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()
