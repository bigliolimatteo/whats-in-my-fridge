from datetime import date

class GenericFoodStorage:
    def __init__(self, name, capacity, foods):
        self.name = name
        self.capacity = capacity 
        self.foods = foods

    def add_food(self, new_food):
        for f in new_food:
            if self.capacity > len(self.foods):
                self.foods.append(f)
                self.capacity -= f.quantity       

    def remove_food(self, consumed_food, consumed_quantity):
        for f in self.foods:
            if f.name == consumed_food.name and consumed_quantity == f.quantity:
                self.foods.remove(consumed_food)
                self.capacity += consumed_quantity
            elif consumed_quantity < f.quantity:
                f.quantity -= consumed_quantity    
                self.capacity += consumed_quantity
                return f
            else:
                raise Exception("You cannot consume more than you have!")
    
    def food_availability(self, new_date):
        available_food = []
        for food in self.foods:
            if food.purchase_date <= new_date and food.expiration_date >= new_date:
                available_food.append((food.name, food.quantity))           
            return available_food
       
    def get_quantity_and_name(self):
        for f in self.foods:
            print(f.name, f.quantity)
            
    def __str__(self):
        return f'{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}'
