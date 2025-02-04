from generic_food import GenericFood
from datetime import datetime

class GenericFoodStorage:
    def __init__(self, name: str, capacity: float, foods: dict[GenericFood, int]):
        self._name = name
        self._capacity = capacity
        self._foods = foods

    def reduce_capacity(self, added_quantity):
        self._capacity -= added_quantity

    def increase_capacity(self, consumed_quantity):
        self._capacity += consumed_quantity
    
    def increase_quantity(self, food: GenericFood, quantity: int):
        if food.name in self._foods:
            if quantity < self._capacity:
                self._foods[food.name].quantity += quantity
                self.reduce_capacity(quantity)
            else:
                raise Exception("You don't have enough space to store this food!")
        else:
            raise Exception(f"No {food} in the storage!")
    
    def add_food(self, new_food: GenericFood, quantity: int):

        if new_food.name not in self._foods and quantity <= self._capacity:
            self._foods.update({new_food.name: quantity})
            self.reduce_capacity(quantity)
        else:
            self.increase_quantity(new_food, quantity)

    
    def consume_food(self, food_to_consume: GenericFood, quantity_to_consume: int):            
        if food_to_consume.name in self._foods:
            if quantity_to_consume > self._foods[food_to_consume.name]:
                raise Exception("You cannot consume more than you have!")
            elif quantity_to_consume == self._foods[food_to_consume.name]:
                del self._foods[food_to_consume.name]
                self.increase_capacity(quantity_to_consume)
            else:
                self._foods[food_to_consume.name] -= quantity_to_consume
                self.increase_capacity(quantity_to_consume)
        else:
            raise Exception(f"There is no {food_to_consume} in the storage!")
    
    def get_food_on_date(self, date: datetime):
        if not isinstance(date, datetime):
            raise ValueError("The argument must be a datetime object.")
        
        return {food: quantity for food, quantity in self._foods.items() if food.expiration_date >= date}
        

    def __str__(self):
        return f"{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}"
