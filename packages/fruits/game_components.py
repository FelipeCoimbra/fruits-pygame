import abc,sys
import pygame
from fruits.utils import load_image

from typing import Tuple


class Mesh(abc.ABC):

    def __init__(self,
                 image: str,
                 position: Tuple[int, int] = None,
                 orientation: float = None,
                 speed: float = None) -> None:
        self.position = position
        self.orientation = orientation
        self.speed = speed
        self.image = self.image = load_image(image)
        self.rect = self.image.get_rect()

    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()

    def draw_on(self, screen) -> None:
        screen.blit(self.image, self.position)


class Collider(pygame.sprite.Sprite, abc.ABC):

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)


class RigidBody(abc.ABC):

    def __init__(self, parameters) -> None:
        for key, value in parameters.items():
            setattr(self, key, value)
        print(self.mass)


class GameComponents(RigidBody, Mesh, Collider):

    def set_component(self,
                      component: str,
                      **kwargs) -> None:
        getattr(sys.modules[__name__], component).__init__(self, **kwargs)
        self._update_world()

    def _update_world(self):
        pass
