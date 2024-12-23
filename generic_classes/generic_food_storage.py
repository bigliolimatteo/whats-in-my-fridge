class GenericFoodStorage:
    def __init__(self, name: str, capacity: float, foods: list):
        self.name = name
        if capacity > 0:
            self.capacity = capacity
        self.foods = foods

    def reduce_capacity(self, consumed_quantity):
        self.capacity -= consumed_quantity
    
    def increase_capacity(self, added_quantity):
        self.capacity += added_quantity
    
    def add_food(self, new_food):
        for f in new_food:
            if self.capacity >= f.quantity:
                self.foods.append(f)
                self.reduce_capacity(f.quantity)
            elif self.capacity < f.quantity:
                raise Exception("You don't have enough space to store this food!")   

    def consume_food(self, consumed_food, consumed_quantity):
        for f in self.foods:
            if f.name == consumed_food.name and consumed_quantity == f.quantity:
                self.foods.remove(consumed_food)
                self.increase_capacity(consumed_quantity) 
            elif f.name == consumed_food.name and consumed_quantity < f.quantity:
                f.quantity -= consumed_quantity    
                self.increase_capacity(consumed_quantity) 
            elif f.name == consumed_food.name and consumed_quantity > f.quantity:
                raise Exception("You cannot consume more than you have!")
    
    def food_availability(self, new_date):
        return [(food.name, food.quantity) for food in self.foods if food.purchase_date <= new_date and food.expiration_date >= new_date]
    
    def get_quantity_and_name(self):
        for f in self.foods:
            print(f.name, f.quantity)
            
    def __str__(self):
        return f'{self.name} with capacity: {self.capacity}, containing: {[str(f) for f in self.foods]}'
