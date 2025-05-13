from dataclasses import dataclass, field


@dataclass(slots=True, order=True)
class Employee:
    sort_index: int = field(init=False, repr=False)
    name: str = field(compare=False)
    email: str = field(compare=False)
    department: str = field(compare=False)
    hours: int = field(compare=False)
    rate: int = field(compare=False)
    payout: int = field(init=False)

    def __post_init__(self):
        self.payout = self.hours * self.rate
        self.sort_index = self.payout

    def __str__(self):
        return f'{self.name} {self.department}'
