import unittest

from generic_classes.nutritional_info import NutritionalInformation


class TestNutritionalInfo(unittest.TestCase):

    def test_nutritional_info_creation(self):
        nutritional_info = NutritionalInformation(
            total_kcal=200,
            total_fat=10,
            total_proteins=5,
            total_carbs=30,
            total_sugar=20,
        )
        self.assertEqual(nutritional_info.total_kcal, 200)
        self.assertEqual(nutritional_info.total_fat, 10)
        self.assertEqual(nutritional_info.total_proteins, 5)
        self.assertEqual(nutritional_info.total_carbs, 30)
        self.assertEqual(nutritional_info.total_sugar, 20)


if __name__ == "__main__":
    unittest.main()
