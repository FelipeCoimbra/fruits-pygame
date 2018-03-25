from fruits.controllers.controller import Controller
from fruits.command import Command


class MatchController(Controller):

    def __init__(self, match_entity):
        super(MatchController, self).__init__(match_entity)
        self.events = [Command.QUIT, Command.TAB_START]

    def listening_events(self):
        return self.events

    def receive(self, command):
        if command == Command.QUIT:
            self.entity.interrupt()
