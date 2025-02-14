import unittest
from datetime import datetime

from generic_classes.generic_food_storage import GenericFoodStorage
from generic_classes.generic_food import GenericFood


class TestFruit(GenericFood):
    def calculate_food_volume(self, quantity: float) -> float:
        return 0 if 0 < quantity < 5 else 1


class TestGenericFoodStorage(unittest.TestCase):
    def setUp(self):
        self.banana = TestFruit(name="Banana", expiration_date=datetime(2024, 12, 10))
        self.fridge = GenericFoodStorage(
            name="Fridge", capacity=10, foods={self.banana: 2}
        )

    def test_storage_initialization(self):
        self.assertEqual(self.fridge.name, "Fridge")
        self.assertEqual(self.fridge.capacity, 10)
        self.assertEqual(len(self.fridge.foods), 1)

    def test_increase_quantity(self):
        self.fridge.add_food(self.banana, 3)
        self.assertEqual(self.fridge.foods, {self.banana: 5})
        self.assertEqual(self.fridge.capacity, 9)

    def test_add_food(self):
        apple = TestFruit(name="Apple", expiration_date=datetime(2024, 11, 10))
        self.fridge.add_food(apple, 5)
        self.assertEqual(len(self.fridge.foods), 2)
        self.assertEqual(self.fridge.capacity, 9)
        with self.assertRaises(Exception):
            self.fridge.add_food(apple, 12, 12)

    def test_consume_food(self):
        self.fridge.consume_food(self.banana, 1)
        self.assertEqual(self.fridge.foods, {self.banana: 1})
        self.assertEqual(self.fridge.capacity, 10)

    def test_consume_food_insufficient_quantity(self):
        with self.assertRaises(Exception):
            self.fridge.consume_food(self.banana, 6, 2)

    def test_get_food_on_date(self):
        available_foods = self.fridge.get_food_on_date(datetime(2024, 11, 2))
        self.assertEqual(len(available_foods), 1)
        self.assertEqual(available_foods, {self.banana: 2})


if __name__ == "__main__":
    unittest.main()
