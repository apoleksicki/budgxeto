from typing import List
from unittest import TestCase

from budgxeto.cli import create_add_expense
from budgxeto.generic import Command
from budgxeto.generic import CommandHandler


class TestAddExpense(TestCase):
    def test_calls_handler_with_command(self) -> None:
        command_handler = SpyCommandHandler()
        add_expense = create_add_expense(handler=command_handler)
        add_expense(amount='100')
        self.assertTrue(command_handler.commands)


class SpyCommandHandler(CommandHandler):
    def __init__(self) -> None:
        self.commands: List[Command] = []

    def handle(self, command: Command) -> None:
        self.commands.append(command)
