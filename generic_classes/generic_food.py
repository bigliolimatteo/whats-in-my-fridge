from dataclasses import dataclass
from datetime import datetime


@dataclass
class GenericFood:
    name: str
    expiration_date: datetime

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def expiration_date(self) -> datetime:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime) -> None:
        self._expiration_date = expiration_date

    def __str__(self) -> str:
        return f"Type of food: {self._name}, expiration date: {self._expiration_date}"

    def __hash__(self) -> int:
        return hash((self._name, self._expiration_date))
