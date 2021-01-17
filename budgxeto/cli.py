import sys


def add_expense(amount: str) -> None:
    pass


def list_expenses() -> None:
    print('Expenses:')
    print('100')


def main() -> None:
    if sys.argv[1] == 'add-expense':
        add_expense('50')

    if sys.argv[1] == 'list-expenses':
        list_expenses()
