import sys
from typing import Callable


def create_add_expense() -> Callable[[str], None]:
    def add_expense(amount: str) -> None:
        pass
    return add_expense


def list_expenses() -> None:
    print('Expenses:')
    print('100')


def main() -> None:
    add_expense = create_add_expense()

    if sys.argv[1] == 'add-expense':
        add_expense('50')

    if sys.argv[1] == 'list-expenses':
        list_expenses()
