from dataclasses import dataclass
from datetime import datetime


@dataclass
class GenericFood:
    _name: str
    _expiration_date: datetime

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime):
        self._expiration_date = expiration_date

    def __str__(self):
        return f"Type of food: {self._name}, expiration date: {self._expiration_date}"
