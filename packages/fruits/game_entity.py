from abc import ABC, abstractmethod


class GameEntity(ABC):

    def __init__(self):
        self.controller = None

    def attach_controller(self, controller):
        self.controller = controller
