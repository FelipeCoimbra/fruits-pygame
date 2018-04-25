from fruits.controllers.controller import Controller
from fruits.command import Command


class MatchController(Controller):

    def __init__(self, match_entity):
        super(MatchController, self).__init__(match_entity)
        self.events = [Command.QUIT, Command.TAB, Command.Q]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command):
        if command == Command.QUIT:
            self.entity.interrupt()
        if command == Command.TAB:
            self.entity.update_current_fruit()
        if command == Command.Q:
            self.entity.update_current_player()
