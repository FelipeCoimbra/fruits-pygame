import abc,sys
import pygame
from fruits.utils import load_image

from typing import Tuple


class Mesh(pygame.sprite.Sprite, abc.ABC):
    def __init__(self,
                 image: str,
                 width: float,
                 height: float,
                 position: Tuple[int, int] = None,
                 orientation: float = None,
                 vx: float = 0,
                 vy: float = 0,
                 ax: float = 0,
                 ay: float = 0) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.orientation = orientation
        self.position = position
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

        self.__current_image = pygame.transform.scale(load_image(image), (width, height))
        self.__current_image_path = image
        self.__loaded_images = {image: self.__current_image}

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def image(self) -> pygame.Surface:
        return self.__current_image

    @property
    def image_path(self) -> str:
        return self.__current_image_path

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
        self.__current_image_path = image


    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()

    def draw_on(self, screen) -> None:
        screen.blit(self.image, self.position)


class Collider(pygame.sprite.Sprite, abc.ABC):

    def __init__(self) -> None:
        # pygame.sprite.Sprite.__init__(self)
        pass


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
