from fruits.game_components import Collider
import pygame
import copy, math

from fruits.controllers.fruit_controller import FruitController
from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
from fruits.game_components import Mesh
from fruits.geometry.vector2d import Vector2D


class Fruit(GameObject):
    def __init__(self,
                 image: str,
                 position: Vector2D = None) -> None:
        super().__init__(GameObjectTransform(position))

        self.is_selected = False
        self.__walking = False
        self.__jumping = False

        self.attach_controller(FruitController(self))

        self.mesh = Mesh(self, image=image, width=shared.character_width, height=shared.character_height)

        self.collider = Collider(pygame.mask.from_surface(self.mesh.image), self.mesh.rect)

    @property
    def jumping(self):
        return self.__jumping

    @jumping.setter
    def jumping(self, jumping):
        self.__jumping = jumping

    def init(self) -> None:
        pass

    def walk(self, forward: bool) -> None:
        if self.__walking:
            return
        if forward:
            self.velocity += Vector2D.from_polar(4, self.orientation)
            # self.velocity = Vector2D(4*math.cos(self.orientation), 4*math.sin(self.orientation))
        else:
            self.velocity += -1*Vector2D.from_polar(4, self.orientation)
            # self.velocity = Vector2D(-4 * math.cos(self.orientation), -4 * math.sin(self.orientation))
        print("made true")
        self.__walking = True

    def stop_walk(self, forward: bool) -> None:
        if not self.__walking:
            return
        if forward:
            self.velocity -= Vector2D.from_polar(4, self.orientation)
            # self.velocity = Vector2D(4*math.cos(self.orientation), 4*math.sin(self.orientation))
        else:
            self.velocity -= -1*Vector2D.from_polar(4, self.orientation)
            # self.velocity = Vector2D(-4 * math.cos(self.orientation), -4 * math.sin(self.orientation))
        print("made false")
        self.__walking = False

    def jump(self) -> None:
        if self.__jumping:
            return
        self.velocity.y += 20
        self.__jumping = True

    def toggle_selected(self) -> None:
        if self.is_selected:
            self.is_selected = False
            self.mesh.update_image(self.mesh.image_path.replace('happy', 'sad'))
        else:
            self.is_selected = True
            self.mesh.update_image(self.mesh.image_path.replace('sad', 'happy'))
