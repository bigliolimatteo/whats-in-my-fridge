from dataclasses import dataclass
from datetime import datetime


@dataclass
class GenericFood:
    name: str
    expiration_date: datetime

    def __str__(self) -> str:
        return f"Type of food: {self.name}, expiration date: {self.expiration_date}"

    def __hash__(self) -> int:
        return hash((self.name, self.expiration_date))

    def calculate_food_volume(self, quantity: float) -> float:
        raise NotImplementedError("This method must be implemented in the subclass.")
