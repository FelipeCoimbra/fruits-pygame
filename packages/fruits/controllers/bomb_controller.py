from math import atan2, cos, sin

import pygame

from fruits.controllers.controller import Controller
from fruits.command import Command
from fruits.events.explosion import ExplosionEvent


class BombController(Controller):
    listening_events = [
        Command.MOUSE_LEFT_DOWN
        ]
    init_velocity = 100

    def __init__(self, bomb_entity):
        super(BombController, self).__init__(bomb_entity)
        self.angle = 0

    def receive(self, command):
        pos_x, pos_y = self.entity.mesh.position
        if command == Command.MOUSE_LEFT_DOWN:
            mos_x, mos_y = pygame.mouse.get_pos()
            self.angle = atan2(mos_y - pos_y, mos_x - pos_x)
            print('>>>>>>>>>> Launching bomb! <<<<<<<<<<')
            print(f'>>> Bomb position: {self.entity.mesh.position}')
            print(f'>>> Mouse position: {pygame.mouse.get_pos()}')
            print(f'>>> Angle: {self.angle}')
            self.launch()

    def explode(self) -> None:
        print('<<<<<<<<<< EXPLODING >>>>>>>>>>')
        explode_event = pygame.event.Event(pygame.USEREVENT,
                                           {'position': self.entity.mesh.position,
                                            'event_class': ExplosionEvent,
                                            'bomb': self.entity})

        pygame.event.post(explode_event)

    def launch(self) -> None:
        self.entity.mesh.vx = self.init_velocity * cos(self.angle)
        self.entity.mesh.vy = self.init_velocity * sin(self.angle)
