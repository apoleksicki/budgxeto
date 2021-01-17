from abc import ABC
from abc import abstractmethod


class Command:
    pass


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command: Command) -> None:
        pass


class Event:
    pass
