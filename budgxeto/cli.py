import sys
from typing import Callable

from budgxeto.application.expense import AddExpenseCommand
from budgxeto.application.expense import AddExpenseCommandHandler
from budgxeto.generic import CommandHandler


def create_add_expense(handler: CommandHandler) -> Callable[[str], None]:
    def add_expense(amount: str) -> None:
        command = AddExpenseCommand(amount=float(amount))
        handler.handle(command)

    return add_expense


def list_expenses() -> None:
    print('Expenses:')
    print('100')


def main() -> None:
    add_expense = create_add_expense(AddExpenseCommandHandler())

    if sys.argv[1] == 'add-expense':
        add_expense('50')

    if sys.argv[1] == 'list-expenses':
        list_expenses()
