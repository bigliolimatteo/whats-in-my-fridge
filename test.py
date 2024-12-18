from generic_food import GenericFood

if __name__ == "__main__":
    banana = GenericFood(name="Banana", purchase_date="2023-10-01", expiration_date="2023-12-10", quantity=1)
    print(banana)
    banana.consume_food(2)
    print(banana)