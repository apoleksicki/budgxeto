from typing import List

from budgxeto.domain.events.expense import ExpenseAdded
from budgxeto.generic import Event


class Expense:
    def __init__(self) -> None:
        amount: float
        self._events: List[Event] = []

    @classmethod
    def create(cls, amount: float) -> 'Expense':
        expense = cls()
        expense.apply(ExpenseAdded(amount=amount))
        return expense

    def apply(self, event: Event) -> None:
        if isinstance(event, ExpenseAdded):
            self.amount = event.amount

        self._events.append(event)

    def changes(self) -> List[Event]:
        return self._events
