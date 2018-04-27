from fruits.controllers.controller import Controller
from fruits.command import Command


class MenuController(Controller):

    def __init__(self, match_entity):
        super(MenuController, self).__init__(match_entity)
        self.quit_events = [Command.QUIT, Command.Q]
        self.events = [Command.QUIT, Command.Q, Command.ENTER]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command):
        if command in self.quit_events:
            self.entity.interrupt()
        if command == Command.ENTER:
            self.entity.new_match()


