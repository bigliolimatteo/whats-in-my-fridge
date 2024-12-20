from generic_food import GenericFood
from generic_food_storage import GenericFoodStorage
from datetime import datetime

if __name__ == "__main__":
    banana = GenericFood(name="Banana", purchase_date=datetime(2024, 10, 1), expiration_date=datetime(2024, 12, 10), quantity=5)
    apple = GenericFood(name="Apple", purchase_date=datetime(2024, 10, 1), expiration_date=datetime(2024, 12, 10), quantity=6)
    strawberry = GenericFood(name="Strawberry", purchase_date=datetime(2024, 10, 1), expiration_date=datetime(2024, 12, 10), quantity=2)
    fruit = [banana, apple, strawberry]
   
    fridge = GenericFoodStorage(name="Fridge", capacity=50, foods=[])
    #print(fridge)
    fridge.add_food(fruit)
    print(fridge)

    