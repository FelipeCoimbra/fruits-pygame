

class EventHandler:

    def __init__(self):
        self.__controllers = []
        self.__commands = []

    #TODO: Create unsubscribe_controller
    def subscribe_controller(self, controller) -> None:
        self.__controllers.append(controller)

    def notify_commands(self) -> None:
        for command in self.__commands:
            for controller in self.__controllers:
                controller.execute_command(command)