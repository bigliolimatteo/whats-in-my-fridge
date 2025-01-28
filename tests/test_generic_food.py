import sys
import os

# Add the parent directory of 'generic_classes' to the Python path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..", "whats-in-my-fridge")
    ),
)
import unittest
from datetime import datetime
from generic_classes.generic_food import GenericFood


class TestGenericFood(unittest.TestCase):

    def test_generic_food_creation(self):
        banana = GenericFood(
            name="Banana",
            purchase_date=datetime(2024, 10, 1),
            expiration_date=datetime(2024, 12, 10),
            quantity=5,
        )
        self.assertEqual(banana.name, "Banana")
        self.assertEqual(banana.purchase_date, datetime(2024, 10, 1))
        self.assertEqual(banana.expiration_date, datetime(2024, 12, 10))
        self.assertEqual(banana.quantity, 5)

    def test_generic_food_invalid_expiration_date(self):
        with self.assertRaises(Exception) as context:
            GenericFood(
                name="Banana",
                purchase_date=datetime(2024, 10, 1),
                expiration_date=datetime(2024, 9, 30),
                quantity=5,
            )
        self.assertEqual(
            str(context.exception), "Expiration date must be after purchase date!"
        )

    def test_generic_food_invalid_quantity(self):
        with self.assertRaises(Exception) as context:
            GenericFood(
                name="Banana",
                purchase_date=datetime(2024, 10, 1),
                expiration_date=datetime(2024, 12, 10),
                quantity=-1,
            )
        self.assertEqual(str(context.exception), "Quantity must be greater than 0!")

    def test_modify_quantity(self):
        banana = GenericFood(
            name="Banana",
            purchase_date=datetime(2024, 10, 1),
            expiration_date=datetime(2024, 12, 10),
            quantity=5,
        )
        banana.modify_quantity(10)
        self.assertEqual(banana.quantity, 10)


if __name__ == "__main__":
    unittest.main()
