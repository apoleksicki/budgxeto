from dataclasses import dataclass

from budgxeto.generic import Event


@dataclass(frozen=True)
class ExpenseAdded(Event):
    amount: float
