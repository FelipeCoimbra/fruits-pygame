from typing import Tuple
from fruits.game_components import Collider
import pygame

from fruits.geometry.vector2d import Vector2D
from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
from fruits.game_components import Mesh


class ExplosionEffect(GameObject):
    always_update = True

    def __init__(self,
                 position: Vector2D = None,
                 orientation: float = None,
                 velocity: Vector2D = None) -> None:
        super().__init__(GameObjectTransform(position=position, velocity=velocity,
                                             orientation=orientation))

        size = shared.character_width * 4
        # pos = tuple(map(lambda x: int(x - size / 2), pos))
        self.position -= Vector2D(size / 2, size / 2)

        self.frame_count = 0
        self.mesh = Mesh(game_object=self, image='red_circle.png', width=size, height=size)

    def init(self) -> None:
        pass

    def update(self) -> None:
        pass

    def update_frame(self) -> None:
        self.frame_count += 1
        if self.should_fade():
            event = pygame.event.Event(pygame.USEREVENT,
                                       {'event_class': ExplosionEffectEvent,
                                        'entity': self})
            pygame.event.post(event)

    def should_fade(self) -> bool:
        return self.frame_count >= .3 * 60

    def move(self, collided: bool) -> None:
        pass

    def update_selected_status(self):
        pass


class ExplosionEffectEvent:
    def __init__(self, explosion_effect: ExplosionEffect) -> None:
        self.explosion_effect = explosion_effect

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'
