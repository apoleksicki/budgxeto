from dataclasses import dataclass

from budgxeto.generic import Command
from budgxeto.generic import CommandHandler


@dataclass(frozen=True)
class AddExpenseCommand(Command):
    amount: float


class AddExpenseCommandHandler(CommandHandler):
    def handle(self, command: Command) -> None:
        pass
