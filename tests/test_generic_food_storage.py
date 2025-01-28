import sys
import os
# Add the parent directory of 'generic_classes' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'whats-in-my-fridge')))
import unittest
from datetime import datetime
from generic_classes.generic_food_storage import GenericFoodStorage
from generic_classes.generic_food import GenericFood

class TestGenericFoodStorage(unittest.TestCase):
    def setUp(self):
        self.banana = GenericFood(
            name="Banana",
            purchase_date=datetime(2024, 10, 1),
            expiration_date=datetime(2024, 12, 10),
            quantity=5,
        )
        self.fridge = GenericFoodStorage(
            name="Fridge", capacity=10, foods=[self.banana]
        )

    def test_add_food(self):
        apple = GenericFood(
            name="Apple",
            purchase_date=datetime(2024, 11, 2),
            expiration_date=datetime(2024, 11, 10),
            quantity=5,
        )
        self.fridge.add_food([apple])
        self.assertEqual(len(self.fridge._foods), 2)
        self.assertEqual(self.fridge._capacity, 5)

    def test_add_food_insufficient_capacity(self):
        watermelon = GenericFood(
            name="Watermelon",
            purchase_date=datetime(2024, 11, 3),
            expiration_date=datetime(2024, 11, 10),
            quantity=11,
        )
        with self.assertRaises(Exception):
            self.fridge.add_food([watermelon])

    def test_consume_food(self):

        self.fridge.consume_food(self.banana, 2)
        self.assertEqual(self.banana.quantity, 3)
        self.assertEqual(self.fridge._capacity, 12)

    def test_consume_food_insufficient_quantity(self):
        with self.assertRaises(Exception):
            self.fridge.consume_food(self.banana, 6)

    def test_food_availability(self):
        available_foods = self.fridge.food_availability(datetime(2024, 11, 2))
        self.assertEqual(len(available_foods), 1)

    def test_increase_capacity(self):
        self.fridge.increase_capacity(2)
        self.assertEqual(self.fridge._capacity, 12)

    def test_initialization(self):
        self.assertEqual(self.fridge._name, "Fridge")
        self.assertEqual(self.fridge._capacity, 10)
        self.assertEqual(len(self.fridge._foods), 1)

    def test_reduce_capacity(self):
        self.fridge.reduce_capacity(2)
        self.assertEqual(self.fridge._capacity, 8)


if __name__ == "__main__":
    unittest.main()
