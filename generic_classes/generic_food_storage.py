from generic_classes.generic_food import GenericFood
from datetime import datetime


class GenericFoodStorage:
    def __init__(
        self,
        name: str,
        capacity: int,
        foods: dict[GenericFood, float],
        food_volume: int,
    ):
        self._name = name
        self._capacity = capacity
        self._foods = foods
        self._food_volume = food_volume

    def decrease_capacity(self, added_volume) -> None:
        self._capacity -= added_volume

    def increase_capacity(self, consumed_volume) -> None:
        self._capacity += consumed_volume

    def increase_quantity(
        self, food: GenericFood, quantity: int, food_volume: int
    ) -> None:
        if food in self._foods:
            if food_volume < self._capacity:
                self._foods[food] += quantity
                self.decrease_capacity(food_volume)
            else:
                raise Exception("You don't have enough space to store this food!")
        else:
            raise Exception(f"No {food} in the storage!")

    def add_food(
        self, new_food: GenericFood, quantity: float, food_volume: int
    ) -> None:
        if new_food not in self._foods and food_volume <= self._capacity:
            self._foods.update({new_food: quantity})
            self.decrease_capacity(food_volume)
        else:
            self.increase_quantity(new_food, quantity, food_volume)

    def consume_food(
        self,
        food_to_consume: GenericFood,
        quantity_to_consume: float,
        food_volume_to_consume: int,
    ) -> None:
        if food_to_consume in self._foods:
            if quantity_to_consume > self._foods[food_to_consume]:
                raise Exception("You cannot consume more than you have!")
            elif quantity_to_consume == self._foods[food_to_consume]:
                del self._foods[food_to_consume]
                self.increase_capacity(food_volume_to_consume)
            else:
                self._foods[food_to_consume] -= quantity_to_consume
                self.increase_capacity(food_volume_to_consume)
        else:
            raise Exception(f"There is no {food_to_consume} in the storage!")

    def get_food_on_date(self, date: datetime):
        if not isinstance(date, datetime):
            raise ValueError("The argument must be a datetime object.")

        return {
            food: quantity
            for food, quantity in self._foods.items()
            if food.expiration_date >= date
        }

    def __str__(self):
        return f"{self._name} with capacity: {self._capacity}, containing: {[str(f) for f in self._foods]}"
