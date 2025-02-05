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
        self.name = name
        self.capacity = capacity
        self.foods = foods
        self.food_volume = food_volume

    def decrease_capacity(self, added_volume) -> None:
        self.capacity -= added_volume

    def increase_capacity(self, consumed_volume) -> None:
        self.capacity += consumed_volume

    def add_food(
        self, new_food: GenericFood, quantity: float, food_volume: int
    ) -> None:
        if new_food in self.foods:
            if food_volume <= self.capacity:
                self.foods[new_food] += quantity
                self.decrease_capacity(food_volume)
            else:
                raise Exception("You don't have enough space to store this food!")
        elif new_food not in self.foods and food_volume <= self.capacity:
            self.foods.update({new_food: quantity})
            self.decrease_capacity(food_volume)
        else:
            raise Exception("You don't have enough space to store this food!")

    def consume_food(
        self,
        food_to_consume: GenericFood,
        quantity_to_consume: float,
        food_volume_to_consume: int,
    ) -> None:
        if food_to_consume in self.foods:
            if quantity_to_consume > self.foods[food_to_consume]:
                raise Exception("You cannot consume more than you have!")
            elif quantity_to_consume == self.foods[food_to_consume]:
                del self.foods[food_to_consume]
                self.increase_capacity(food_volume_to_consume)
            else:
                self.foods[food_to_consume] -= quantity_to_consume
                self.increase_capacity(food_volume_to_consume)
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
