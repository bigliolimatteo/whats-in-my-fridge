from datetime import date

class GenericFoodStorage:
    def __init__(self, name, capacity, foods):
        self.name = name
        self.capacity = capacity 
        self.foods = foods

    def add_food(self, new_food =[]):
        for f in new_food:
            if self.capacity >= len(self.foods) + 1:
                self.foods.append(f)
                self.capacity -= f.quantity
                return self.foods, self.capacity
            else:
                return False

    def remove_food(self, consumed_food=[]):
        for f in consumed_food:
            self.foods.remove(f)
            self.capacity += f.quantity
            return self.foods, self.capacity
        else:
            return False
    
    def food_availability(self, new_date):
        available_food = []
        for food in self.foods:
            if food.purchase_date <= date.fromisoformat(new_date) and food.expiration_date >= date.fromisoformat(new_date):
                available_food.append((food.name, food.quantity))           
            return available_food
       
    def get_quantity_and_name(self):
        for f in self.foods:
            return f.name, f.quantity

    def __str__(self):
        return f'{self.name} with capacity: {self.capacity}, containing: {self.get_quantity_and_name()}'
