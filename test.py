from generic_food import GenericFood
from generic_food_storage import GenericFoodStorage
from datetime import datetime

if __name__ == "__main__":
    banana = GenericFood(name="Banana", purchase_date=datetime(2024, 10, 1), expiration_date=datetime(2024, 12, 10), quantity=5)
    apple = GenericFood(name="Apple", purchase_date=datetime(2024, 10, 1), expiration_date=datetime(2024, 12, 10), quantity=6)
    fruit = [banana, apple]
    #print(banana)
    #banana.consume_food(2)
    #print(banana)

    fridge = GenericFoodStorage(name="Fridge", capacity=50, foods=[])
    #print(fridge)
    fridge.add_food(fruit)
    print(fridge)
    available_food = fridge.food_availability(datetime(2024, 11, 1))
    print(available_food)
    fridge.remove_food(banana, 2)
    print(fridge)
    available_food = fridge.food_availability(datetime(2024, 10, 1))
    print(available_food)