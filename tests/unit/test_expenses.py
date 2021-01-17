from unittest import TestCase

from budgxeto.cli import create_add_expense


class TestAddExpense(TestCase):
    def test_accepts_amount(self) -> None:
        add_expense = create_add_expense()
        add_expense(amount='100')
