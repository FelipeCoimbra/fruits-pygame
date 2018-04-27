from typing import Dict, List, Iterable

import pygame

from fruits.command import Command
from fruits.controllers.controller import Controller
from fruits.game_entity import GameEntity
from fruits.events.explosion import ExplosionEvent
from fruits.explosion_effect import ExplosionEffectEvent


class EventHandler:
    def __init__(self):
        self.__subscriptions: Dict[str, List[Controller]] = {}
        self.__hold_subscriptions: Dict[str, List[Controller]] = {}
        self.__hold_events = set()

    def subscribe_entity(self, entity: GameEntity):
        if entity.controller is not None:
            self.__subscribe_controller(entity.controller)

    def unsubscribe_entity(self, entity: GameEntity):
        if entity.controller is not None:
            for events in self.__subscriptions:
                try:
                    self.__subscriptions[events].remove(entity.controller)
                except ValueError:
                    continue

    def __subscribe_controller(self, controller: Controller) -> None:
        for event in controller.listening_events:
            if self.__subscriptions.get(event):
                self.__subscriptions[event].append(controller)
            else:
                self.__subscriptions[event] = [controller]

    def process_events(self, events: Iterable[str]) -> None:
        for event in events:
            subscriptions = self.get_subscriptions(event)

            if event != 'MOUSEMOTION':
                print(f'Got event: {event}')

                if isinstance(event, ExplosionEffectEvent):
                    1 + 1

            if subscriptions is not None:
                self.publish_event(event, subscriptions)
                if (isinstance(event, str)
                        and event.endswith('START') 
                        and event != 'SPACE_START'):
                    self.__hold_events.add(event)
            if isinstance(event, str) and event.endswith('END'):
                self.__hold_events.discard(event.replace('END', 'START'))

        self.process_hold_events()

    def process_hold_events(self) -> None:
        for event in self.__hold_events:
            subscriptions = self.get_subscriptions(event)
            # print('Event: %15s - Subscriptions: %s' % (event, subscriptions))

            if subscriptions is not None:
                self.publish_event(event, subscriptions)

    # @staticmethod
    def publish_event(self, event, subscriptions: List[Controller]) -> None:
        for subscription in subscriptions:
            subscription.receive(event)

    def get_subscriptions(self, event):
        if not isinstance(event, str):
            subscriptions = self.__subscriptions.get(type(event))
        else:
            subscriptions = self.__subscriptions.get(event)

        return subscriptions
