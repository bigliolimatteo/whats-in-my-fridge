from dataclasses import dataclass
from generic_classes.generic_food import GenericFood


@dataclass
class GenericFoodStorage:
    def __init__(self, name: str, capacity: float, foods: list[GenericFood]):
        self._name = name
        self._capacity = capacity
        self._foods = list(foods)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        assert value >= 0, "Capacity must be greater than 0!"
        self._capacity = value

    @property
    def foods(self):
        return self._foods

    @foods.setter
    def foods(self, value):
        self._foods = value

    def reduce_capacity(self, consumed_quantity):
        self.capacity -= consumed_quantity

    def increase_capacity(self, added_quantity):
        self.capacity += added_quantity

    def add_food(self, new_food: list[foods]):
        total_quantity = sum(f.quantity for f in new_food)
        if self.capacity >= total_quantity:
            self.foods.extend(new_food)
            self.reduce_capacity(total_quantity)
        else:
            raise Exception("You don't have enough space to store this food!")

    def consume_food(self, consumed_food: dict["food":str, "quantity":float]):
        for f in self.foods:
            consumed_foodtype = consumed_food.get("food")
            consumed_quantity = consumed_food.get("quantity")

            if f.name == consumed_foodtype and f.quantity == consumed_quantity:
                self.foods.remove(f)
                self.increase_capacity(consumed_quantity)
            elif f.name == consumed_foodtype and consumed_quantity < f.quantity:
                f.quantity -= consumed_quantity
                self.increase_capacity(consumed_quantity)
            elif f.name == consumed_foodtype and consumed_quantity > f.quantity:
                raise Exception("You cannot consume more than you have!")
            else:
                raise Exception(f"No {consumed_foodtype} in the storage!")

    def food_availability(self, date):
        return [
            (food.name, food.quantity)
            for food in self.foods
            if food.purchase_date <= date and food.expiration_date >= date
        ]

    def __str__(self):
        return f"{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}"
