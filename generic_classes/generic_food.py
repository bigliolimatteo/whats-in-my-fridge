from dataclasses import dataclass
from datetime import datetime


@dataclass
class GenericFood:
    name: str
    purchase_date: datetime
    expiration_date: datetime
    quantity: float

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, value):
        self._purchase_date = value

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        assert (
            value >= self.purchase_date
        ), "Expiration date must be after purchase date!"
        self._expiration_date = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        assert value > 0, "Quantity must be greater than 0!"
        self._quantity = value

    def modify_quantity(self, new_quantity):
        if new_quantity is not None and new_quantity > 0:
            self.quantity = new_quantity

    def __str__(self):
        return f"Type of food: {self.name}, purchased on: {self.purchase_date}, expiration date: {self.expiration_date}, quantity: {self.quantity}"
