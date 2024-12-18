from generic_food import GenericFood

class GenericFoodStorage:
    def __init__(self, name, capacity, foods):
        self.name = name
        self.capacity = capacity 
        self.foods = foods

    def add_food(self, food):
        if self.capacity >= len(self.foods) + 1:
            self.foods.append(food)
            return True
        else:
            return False

    def remove_food(self, food):
        if food in self.foods:
            self.foods.remove(food)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} has {len(self.foods)} food items"
