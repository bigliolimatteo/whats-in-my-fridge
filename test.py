from generic_food import GenericFood
from generic_food_storage import GenericFoodStorage

if __name__ == "__main__":
    banana = GenericFood(name="Banana", purchase_date="2023-10-01", expiration_date="2023-12-10", quantity=5)
    apple = GenericFood(name="Apple", purchase_date="2024-10-01", expiration_date="2024-12-10", quantity=6)
    fruit = [banana, apple]
    eaten_banana = [banana]
    #print(banana)
    banana.consume_food(2)
    #print(banana)

    fridge = GenericFoodStorage(name="Fridge", capacity=5, foods=[])
    #print(fridge)
    fridge.add_food(fruit)
    #print(fridge)
    available_food = fridge.food_availability("2023-11-01")
    print(available_food)
    fridge.remove_food(eaten_banana)
    #print(fridge)
    available_food = fridge.food_availability("2023-11-01")
    #print(available_food)