from generic_classes.generic_food import GenericFood


class GenericFoodStorage:
    def __init__(self, name: str, capacity: float, foods: dict[GenericFood, float]):
        self._name = name
        self._capacity = capacity
        self._foods = list(foods)

    def get_name(self) -> str:
        return self._name

    def get_capacity(self) -> float:
        return self._capacity

    def get_foods(self) -> dict["food":GenericFood, "quantity":float]:
        return self._foods

    def reduce_capacity(self, added_quantity):
        self._capacity -= added_quantity

    def increase_capacity(self, consumed_quantity):
        self._capacity += consumed_quantity

    def add_food(self, new_food):
        for food in new_food:
            if food.quantity <= self._capacity:
                self._foods.append(food)
                self.reduce_capacity(food.quantity)
            else:
                raise Exception("You don't have enough space to store this food!")

    def consume_food(self, food_to_consume, quantity_to_consume):
        if food_to_consume not in self._foods:
            raise Exception(f"No {food_to_consume} in the storage!")

        food = self._foods[self._foods.index(food_to_consume)]

        if quantity_to_consume > food.quantity:
            raise Exception("You cannot consume more than you have!")
        elif quantity_to_consume == food.quantity:
            self._foods.remove(food)
        else:
            food.quantity -= quantity_to_consume

        self.increase_capacity(quantity_to_consume)

    def food_availability(self, date):
        return [
            (food.name, food.quantity)
            for food in self._foods
            if food.purchase_date <= date and food.expiration_date >= date
        ]

    def __str__(self):
        return f"{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}"
