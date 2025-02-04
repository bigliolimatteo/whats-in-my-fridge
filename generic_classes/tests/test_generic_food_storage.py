import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
from datetime import datetime
from generic_classes.generic_food_storage import GenericFoodStorage
from generic_classes.generic_food import GenericFood


class TestGenericFoodStorage(unittest.TestCase):
    def setUp(self):
        self.banana = GenericFood(
            _name="Banana", _expiration_date=datetime(2024, 12, 10)
        )
        self.fridge = GenericFoodStorage(
            name="Fridge", capacity=10, foods={self.banana: 2}, food_volume=2
        )

    def test_storage_initialization(self):
        self.assertEqual(self.fridge._name, "Fridge")
        self.assertEqual(self.fridge._capacity, 10)
        self.assertEqual(len(self.fridge._foods), 1)
        self.assertEqual(self.fridge._food_volume, 2)

    def test_increase_capacity(self):
        self.fridge.increase_capacity(2)
        self.assertEqual(self.fridge._capacity, 12)

    def test_decrease_capacity(self):
        self.fridge.decrease_capacity(2)
        self.assertEqual(self.fridge._capacity, 8)

    def test_increase_quantity(self):
        self.fridge.increase_quantity(self.banana, 3, 3)
        self.assertEqual(self.fridge._foods, {self.banana: 5})
        self.assertEqual(self.fridge._capacity, 7)

    def test_add_food(self):
        apple = GenericFood(_name="Apple", _expiration_date=datetime(2024, 11, 10))
        self.fridge.add_food(apple, 5, 5)
        self.assertEqual(len(self.fridge._foods), 2)
        self.assertEqual(self.fridge._capacity, 5)
        with self.assertRaises(Exception):
            self.fridge.add_food(apple, 12, 12)

    def test_consume_food(self):
        self.fridge.consume_food(self.banana, 1, 0)
        self.assertEqual(self.fridge._foods, {self.banana: 1})
        self.assertEqual(self.fridge._capacity, 10)

    def test_consume_food_insufficient_quantity(self):
        with self.assertRaises(Exception):
            self.fridge.consume_food(self.banana, 6, 2)

    def test_get_food_on_date(self):
        available_foods = self.fridge.get_food_on_date(datetime(2024, 11, 2))
        self.assertEqual(len(available_foods), 1)
        self.assertEqual(available_foods, {self.banana: 2})


if __name__ == "__main__":
    unittest.main()
