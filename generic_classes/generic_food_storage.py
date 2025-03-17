from generic_classes.generic_food import GenericFood
from datetime import datetime


class GenericFoodStorage:
    def __init__(self, name: str, capacity: float, foods: dict[GenericFood, float]):
        self.name = name
        self._capacity = capacity
        self.foods = foods

    @property
    def capacity(self) -> float:
        return self._capacity - sum(
            f.calculate_food_volume(q) for f, q in self.foods.items()
        )

    @capacity.setter
    def capacity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = value

    def add_food(self, new_food: GenericFood, quantity: float) -> None:
        if (
            new_food in self.foods
            and new_food.calculate_food_volume(quantity) <= self.capacity
        ):
            self.foods[new_food] += quantity
        elif (
            new_food not in self.foods
            and new_food.calculate_food_volume(quantity) <= self.capacity
        ):
            self.foods.update({new_food: quantity})
        else:
            raise Exception("You don't have enough space to store this food!")

    def consume_food(
        self, food_to_consume: GenericFood, quantity_to_consume: float
    ) -> None:
        if food_to_consume in self.foods:
            if quantity_to_consume > self.foods[food_to_consume]:
                raise Exception("You cannot consume more than you have!")
            elif quantity_to_consume == self.foods[food_to_consume]:
                del self.foods[food_to_consume]
            else:
                self.foods[food_to_consume] -= quantity_to_consume
        else:
            raise Exception(f"There is no {food_to_consume} in the storage!")

    def get_food_on_date(self, date: datetime):
        if not isinstance(date, datetime):
            raise ValueError("The argument must be a datetime object.")

        return {
            food: quantity
            for food, quantity in self.foods.items()
            if food.expiration_date >= date
        }

    def __str__(self):
        return f"{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}"

    def __eq__(self, other):

        if isinstance(other, GenericFoodStorage):

            return (
                self.name == other.name
                and self.capacity == other.capacity
                and self.foods == other.foods
            )

        return False
