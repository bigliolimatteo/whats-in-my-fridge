import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from datetime import datetime
from generic_classes.generic_food_storage import GenericFoodStorage
from generic_classes.generic_food import GenericFood

class TestGenericFoodStorage(unittest.TestCase):
    banana = GenericFood(name="Banana", purchase_date=datetime(2024, 11, 1), expiration_date=datetime(2024, 11, 10), quantity=5)
    
    fridge = GenericFoodStorage(name="Fridge", capacity=10, foods=[banana])

    def test_add_food(self):
        apple = GenericFood(name="Apple", purchase_date=datetime(2024, 11, 2), expiration_date=datetime(2024, 11, 10), quantity=5)
        self.fridge.add_food([apple])
        self.assertEqual(len(self.fridge.foods), 2)
        self.assertEqual(self.fridge.capacity, 5)

    def test_add_food_insufficient_capacity(self):
        watermelon = GenericFood(name="Watermelon", purchase_date=datetime(2024, 11, 3), expiration_date=datetime(2024, 11, 10), quantity=10)
        with self.assertRaises(Exception):
            self.fridge.add_food([watermelon])
    
    def test_consume_food(self):
        self.fridge.consume_food(self.banana, 2)
        self.assertEqual(self.banana.quantity, 3)
        self.assertEqual(self.fridge.capacity, 7)
        
    def test_consume_food_insufficient_quantity(self):
        with self.assertRaises(Exception):
            self.fridge.consume_food(self.banana, 6)

    
    def test_food_availability(self):
        available_foods = self.fridge.food_availability(datetime(2024,11,2))
        self.assertEqual(len(available_foods), 2)

    def test_get_quantity_and_name(self):
        self.fridge.get_quantity_and_name()

    def test_increase_capacity(self):
        self.fridge.increase_capacity(2)
        self.assertEqual(self.fridge.capacity, 9)


    def test_initialization(self):
        self.assertEqual(self.fridge.name, "Fridge")
        self.assertEqual(self.fridge.capacity, 9)
        self.assertEqual(len(self.fridge.foods), 2)

    def test_reduce_capacity(self):
        self.fridge.reduce_capacity(2)
        self.assertEqual(self.fridge.capacity, 7)


if __name__ == '__main__':
    unittest.main()