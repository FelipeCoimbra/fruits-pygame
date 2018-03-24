from typing import Dict, List

import pygame

from fruits.command import Command
from fruits.controllers.controller import Controller


class EventHandler:
    def __init__(self):
        self.__subscriptions: Dict[int, List[Controller]] = {}
        self.__hold_subscriptions: Dict[int, List[Controller]] = {}

    def subscribe_controller(self, controller: Controller) -> None:
        for event in controller.listening_events:
            if self.__subscriptions.get(event):
                self.__subscriptions[event].append(controller)
            else:
                self.__subscriptions[event] = [controller]

    def process_events(self, events) -> None:
        for event in events:
            subscriptions = self.__subscriptions.get(event)
            print('Event: %15s - Subscriptions: %s' % (event, subscriptions))

            if event == Command.ESCAPE:
                pygame.quit()
                exit(0)

            if subscriptions is not None:
                self.publish_event(event, subscriptions)

        self.process_hold_events()

    def process_hold_events(self):
        for event, subscriptions in self.__hold_subscriptions.items():
            self.publish_event(event, subscriptions)

    @staticmethod
    def publish_event(event, subscriptions: List[Controller]) -> None:
        for subscription in subscriptions:
            subscription.receive(event)
