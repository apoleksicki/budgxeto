from unittest import TestCase

from budgxeto.generic import Command
from budgxeto.application.expense import AddExpenseCommandHandler


class TestAddExpenseCommandHandler(TestCase):
    def test_accepts_add_expense_command(self) -> None:
        handler = AddExpenseCommandHandler()
        handler.handle(Command())
