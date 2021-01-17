import subprocess
from unittest import TestCase


class TestExpenses(TestCase):
    def test_user_can_add_expense(self) -> None:
        self.user_adds_expense()

    def user_adds_expense(self) -> None:
        result = subprocess.run(['budgxeto', 'add-expense', '100'])
        self.assertEqual(0, result.returncode)
