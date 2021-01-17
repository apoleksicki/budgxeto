from typing import List
from unittest import TestCase

from budgxeto.application.expense import AddExpenseCommand
from budgxeto.cli import create_add_expense
from budgxeto.generic import Command
from budgxeto.generic import CommandHandler


class TestAddExpense(TestCase):
    def test_calls_handler_with_command(self) -> None:
        command_handler = SpyCommandHandler()
        add_expense = create_add_expense(handler=command_handler)
        add_expense(amount='100')
        expected_command = AddExpenseCommand(amount=100.0)
        self.assertEqual(expected_command, command_handler.commands[0])


class SpyCommandHandler(CommandHandler):
    def __init__(self) -> None:
        self.commands: List[Command] = []

    def handle(self, command: Command) -> None:
        self.commands.append(command)
