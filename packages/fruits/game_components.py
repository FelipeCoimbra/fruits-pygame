from fruits.utils import load_image
from abc import ABC
import pygame

from typing import Tuple


class GameComponent(ABC):
    def __init__(self):
        pass

    def update_world(self):
        pass


class Mesh(GameComponent):
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
        super(GameComponent, self).__init__()
        self.orientation = orientation
        self.position = position
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

        self.width = width
        self.height = height

        self.__current_image = pygame.transform.scale(load_image(image), (width, height))
        self.__current_image_path = image
        self.__loaded_images = {image: self.__current_image}

    @property
    def image(self) -> pygame.Surface:
        return self.__current_image

    @property
    def image_path(self) -> str:
        return self.__current_image_path

    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.topleft = self.position
        return rect

    @image.setter
    def image(self, new_image: pygame.Surface) -> None:
        self.__current_image = new_image
        self.__loaded_images[self.__current_image_path] = new_image

    def update_image(self, image: str) -> None:
        loaded = self.__loaded_images.get(image)

        if loaded:
            self.__current_image = loaded
        else:
            image_surface = pygame.transform.scale(load_image(image), (self.width, self.height))

            self.__loaded_images[image] = image_surface
            self.__current_image = image_surface
        self.__current_image_path = image

    def draw_on(self, screen) -> None:
        screen.blit(self.image, self.position)


class Collider(GameComponent, pygame.sprite.Sprite):
    def __init__(self,
                 mask,
                 rect) -> None:
        super(GameComponent, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.__mask = mask
        self.__rect = rect

    @property
    def mask(self):
        return self.__mask

    @property
    def rect(self):
        return self.__rect

    @mask.setter
    def mask(self,
             mask: pygame.mask):
        self.__mask = mask

    @rect.setter
    def rect(self,
             rect):
        self.__rect = rect
