import subprocess
from unittest import TestCase


class TestExpenses(TestCase):
    def test_user_can_add_expense(self) -> None:
        self.user_adds_expense()

    def test_user_can_list_expenses(self) -> None:
        self.user_adds_expense()
        self.user_lists_expenses()

    def user_adds_expense(self) -> None:
        result = subprocess.run(['budgxeto', 'add-expense', '100'])
        self.assertEqual(0, result.returncode)

    def user_lists_expenses(self) -> None:
        result = subprocess.run(
            ['budgxeto', 'list-expenses'], capture_output=True,
        )
        self.assertEqual(0, result.returncode)
        expected_report = (
            'Expenses:\n'
            '100\n'
        )
        self.assertEqual(expected_report, result.stdout.decode())
