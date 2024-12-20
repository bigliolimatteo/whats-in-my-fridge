from datetime import date, datetime

class GenericFood:
    def __init__(self, name: str, purchase_date: datetime, expiration_date: datetime, quantity: float):
        self.name = name
        self.purchase_date = purchase_date
        self.expiration_date = expiration_date
        if quantity > 0:
            self.quantity = quantity
        else:
            raise Exception("Quantity must be greater than 0!")

    def consume_food(self, amount):       
        if amount > self.quantity:
            raise Exception("You cannot consume more than you have!")
        elif amount <= self.quantity:
            self.quantity -= amount

    @classmethod
    def modify_quantity(cls, new_quantity):
        if new_quantity is not None:
            cls.quantity = new_quantity

    def __str__(self):
        food = f'Type of food: {self.name}, purchased on: {self.purchase_date}, expiration date: {self.expiration_date}, quantity: {self.quantity}'
        return food
    
