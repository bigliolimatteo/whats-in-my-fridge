import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
from datetime import datetime
from generic_classes.generic_food import GenericFood


class TestGenericFood(unittest.TestCase):

    def test_generic_food_creation(self):
        banana = GenericFood(name="Banana", expiration_date=datetime(2024, 12, 10))
        self.assertEqual(banana.name, "Banana")
        self.assertEqual(banana.expiration_date, datetime(2024, 12, 10))


if __name__ == "__main__":
    unittest.main()
