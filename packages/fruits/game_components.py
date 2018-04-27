from fruits.utils import load_image
from abc import ABC
import pygame

from typing import Tuple
from fruits.game_object import GameObject


class GameComponent(ABC):
    def __init__(self, game_obj: GameObject) -> None:
        self._game_object = game_obj


class Mesh(GameComponent):
    def __init__(self, game_object: GameObject, image: str, width: float, height: float) -> None:
        super().__init__(game_obj=game_object)

        self.width = width
        self.height = height

        self.__current_image = pygame.transform.scale(load_image(image), (width, height))
        self.__current_image_path = image
        self.__loaded_images = {image: self.__current_image}

        self.rect = self.image.get_rect()
        self.rect.topleft = (self._game_object.position.x, self._game_object.position.y)

    @property
    def image(self) -> pygame.Surface:
        return self.__current_image

    @property
    def image_path(self) -> str:
        return self.__current_image_path

    @property
    def size(self) -> Tuple[int, int]:
        return self.image.get_size()

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
        x = self._game_object.position.x
        y = self._game_object.position.y
        screen.blit(self.image, (x, y))


class Collider(GameComponent, pygame.sprite.Sprite):
    def __init__(self,
                 mask,
                 rect) -> None:
        super(GameComponent, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.__enabled = True
        self.__mask = mask
        self.__rect = rect

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None :
        self.__enabled = enabled

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @rect.setter
    def rect(self, rect) -> None:
        self.__rect = rect

    @property
    def mask(self) -> pygame.mask:
        if self.__enabled:
            return self.__mask

    @mask.setter
    def mask(self, mask: pygame.mask) -> None:
        self.__mask = mask

