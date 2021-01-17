import sys


def add_expense() -> None:
    pass


def list_expenses() -> None:
    print('Expenses:')
    print('100')


def main() -> None:
    if sys.argv[1] == 'add-expense':
        add_expense()

    if sys.argv[1] == 'list-expenses':
        list_expenses()
