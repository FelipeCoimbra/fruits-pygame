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
        self.__current_image = load_image(image)
        self.__current_image_path = 'image'
        self.__loaded_images = {'image': self.__current_image}
        self.rect = self.image.get_rect()

    @property
    def image(self) -> pygame.Surface:
        return self.__current_image

    @image.setter
    def image(self, new_image: pygame.Surface) -> None:
        self.__current_image = new_image
        self.__loaded_images[self.__current_image_path] = new_image

    def update_image(self, image: str) -> None:
        loaded = self.__loaded_images.get(image)

        if loaded:
            self.__current_image = loaded
        else:
            image_surface = load_image(image)
            self.__loaded_images[image] = image_surface
            self.__current_image = image_surface


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
