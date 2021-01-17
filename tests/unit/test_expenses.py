from unittest import TestCase

from budgxeto.cli import add_expense


class TestAddExpense(TestCase):
    def test_accepts_amount(self) -> None:
        add_expense(amount='100')
