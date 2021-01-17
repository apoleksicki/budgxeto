from unittest import TestCase

from budgxeto.cli import create_add_expense
from budgxeto.generic import Command
from budgxeto.generic import CommandHandler


class TestAddExpense(TestCase):
    def test_accepts_amount(self) -> None:
        command_handler = SpyCommandHandler()
        add_expense = create_add_expense(handler=command_handler)
        add_expense(amount='100')


class SpyCommandHandler(CommandHandler):
    def handle(self, command: Command) -> None:
        pass
