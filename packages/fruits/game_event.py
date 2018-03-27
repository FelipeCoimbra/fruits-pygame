from typing import Dict, List, Iterable

import pygame

from fruits.command import Command
from fruits.controllers.controller import Controller
from fruits.game_entity import GameEntity


class EventHandler:
    def __init__(self):
        self.__subscriptions: Dict[str, List[Controller]] = {}
        self.__hold_subscriptions: Dict[str, List[Controller]] = {}
        self.__hold_events = set()

    def subscribe_entity(self, entity: GameEntity):
        if entity.controller is not None:
            self.__subscribe_controller(entity.controller)

    def __subscribe_controller(self, controller: Controller) -> None:
        for event in controller.listening_events:
            if self.__subscriptions.get(event):
                self.__subscriptions[event].append(controller)
            else:
                self.__subscriptions[event] = [controller]

    def process_events(self, events: Iterable[str]) -> None:
        for event in events:
            subscriptions = self.__subscriptions.get(event)
            # print('Event: %15s - Subscriptions: %s' % (event, subscriptions))

            if subscriptions is not None:
                self.publish_event(event, subscriptions)
                if event.endswith('START') and event != 'SPACE_START':
                    self.__hold_events.add(event)
            if event.endswith('END'):
                self.__hold_events.discard(event.replace('END', 'START'))

        self.process_hold_events()

    def process_hold_events(self) -> None:
        for event in self.__hold_events:
            subscriptions = self.__subscriptions.get(event)
            # print('Event: %15s - Subscriptions: %s' % (event, subscriptions))

            if subscriptions is not None:
                self.publish_event(event, subscriptions)

    # @staticmethod
    def publish_event(self, event, subscriptions: List[Controller]) -> None:
        for subscription in subscriptions:
            subscription.receive(event)
