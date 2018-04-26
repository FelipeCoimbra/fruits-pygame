from typing import Tuple
from fruits.game_components import Collider
import pygame

from fruits.game_object import GameObject
import fruits.shared_preferences as shared
from fruits.game_components import Mesh


class ExplosionEffect(GameObject):
    always_update = True

    def __init__(self,
                 position: Tuple[int, int] = (0, 0),
                 orientation: float = None,
                 vx: float = 0,
                 vy: float = 0,
                 ax: float = 0,
                 ay: float = 0) -> None:
        super(GameObject, self).__init__()
        size = shared.character_width * 5
        position = tuple(map(lambda x: int(x - size / 2), position))

        self.frame_count = 0
        self.mesh = Mesh(image='white-circle.png', position=position,
                         orientation=orientation, vx=vx, vy=vy, ax=ax, ay=ay,
                         width=size, height=size)

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
