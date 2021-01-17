import sys
from typing import Callable

from budgxeto.generic import Command
from budgxeto.generic import CommandHandler


def create_add_expense(handler: CommandHandler) -> Callable[[str], None]:
    def add_expense(amount: str) -> None:
        pass
    return add_expense


def list_expenses() -> None:
    print('Expenses:')
    print('100')


def main() -> None:
    class AddExpenseCommandHandler(CommandHandler):
        def handle(self, command: Command) -> None:
            pass

    add_expense = create_add_expense(AddExpenseCommandHandler())

    if sys.argv[1] == 'add-expense':
        add_expense('50')

    if sys.argv[1] == 'list-expenses':
        list_expenses()
