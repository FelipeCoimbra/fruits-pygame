from fruits.controllers.controller import Controller
from fruits.command import Command


class FruitController(Controller):

    def __init__(self, fruit_entity):
        super(FruitController, self).__init__(fruit_entity)
        self.events = [Command.LEFT_START, Command.RIGHT_START,
                       Command.UP_START, Command.DOWN_START]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command):
        if command == Command.LEFT_START:
            self.entity.update(horizontal=-10)
        if command == Command.RIGHT_START:
            self.entity.update(horizontal=10)
        if command == Command.UP_START:
            self.entity.update(vertical=-10)
        if command == Command.DOWN_START:
            self.entity.update(vertical=10)
