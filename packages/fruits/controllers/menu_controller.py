from fruits.controllers.controller import Controller
from fruits.command import Command


class MenuController(Controller):

    def __init__(self, match_entity):
        super(MenuController, self).__init__(match_entity)
        self.events = [Command.TAB]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command):
        if command == Command.TAB:
            self.entity.interrupt()


