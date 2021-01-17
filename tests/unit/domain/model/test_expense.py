from unittest import TestCase

from budgxeto.domain.model.expense import Expense
from budgxeto.domain.events.expense import ExpenseAdded


class TestExpense(TestCase):
    def test_can_be_created(self) -> None:
        amount = 100.0
        expense = Expense.create(amount)
        self.assertEqual([ExpenseAdded(amount)], expense.changes())
        self.assertEqual(amount, expense.amount)
