from datetime import date

class GenericFood:
    def __init__(self, name, purchase_date, expiration_date, quantity):
        self.name = name
        self.purchase_date = date.fromisoformat(purchase_date)
        self.expiration_date = date.fromisoformat(expiration_date)
        self.quantity = quantity

    def consume_food(self, amount):       
        if amount > self.quantity:
            raise Exception("You cannot consume more than you have!")
        elif amount == self.quantity:
            self.quantity -= amount
        else:
            self.quantity -= amount

    @classmethod
    def modify_quantity(cls, new_quantity):
        if new_quantity is not None:
            cls.quantity = new_quantity

    def __str__(self):
        food = f'Type of food: {self.name}, purchased on: {self.purchase_date}, expiration date: {self.expiration_date}, quantity: {self.quantity}'
        return food
    
