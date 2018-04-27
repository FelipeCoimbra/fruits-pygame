from math import atan2, cos, sin

import pygame

from fruits.controllers.controller import Controller
from fruits.command import Command
from fruits.events.explosion import ExplosionEvent, ToggleTeamEvent
from fruits.geometry.vector2d import Vector2D

class BombController(Controller):
    listening_events = [
        Command.MOUSE_LEFT_DOWN
        ]
    init_velocity = 20

    def __init__(self, bomb_entity):
        super(BombController, self).__init__(bomb_entity)
        self.angle = 0

    def receive(self, command):
        pos_x, pos_y = self.entity.position.x, self.entity.position.y
        if command == Command.MOUSE_LEFT_DOWN:
            mos_x, mos_y = pygame.mouse.get_pos()
            self.angle = atan2(mos_y - pos_y, mos_x - pos_x)
            print('>>>>>>>>>> Launching bomb! <<<<<<<<<<')
            print(f'>>> Bomb position: {self.entity.position}')
            print(f'>>> Mouse position: {pygame.mouse.get_pos()}')
            print(f'>>> Angle: {self.angle}')
            self.launch()

    def explode(self) -> None:
        print('<<<<<<<<<< EXPLODING >>>>>>>>>>')
        explode_event = pygame.event.Event(pygame.USEREVENT,
                                           {'position': (self.entity.position.x, self.entity.position.y),
                                            'event_class': ExplosionEvent,
                                            'bomb': self.entity})
        pygame.event.post(explode_event)
        toggle_team_event = pygame.event.Event(pygame.USEREVENT,
                                           {'event_class': ToggleTeamEvent})
        pygame.event.post(toggle_team_event)

    def launch(self) -> None:
        self.entity.velocity = Vector2D.from_polar(self.init_velocity, self.angle)
