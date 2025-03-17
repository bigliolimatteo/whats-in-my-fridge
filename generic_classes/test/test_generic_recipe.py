import unittest
from datetime import datetime
from generic_classes.generic_recipe import GenericRecipe
from generic_classes.nutritional_info import NutritionalInformation


class TestGenericRecipe(unittest.TestCase):

    def test_generic_recipe_creation(self):
        recipe = GenericRecipe(
            name="Banana Bread",
            ingredients={"Banana": 2, "Flour": 1, "Sugar": 1},
            expiration_date=datetime(2024, 12, 10),
            cooking_time=60,
            nutritional_info=NutritionalInformation(
                total_kcal=200,
                total_fat=10,
                total_proteins=5,
                total_carbs=30,
                total_sugar=20,
            ),
        )
        self.assertEqual(recipe.name, "Banana Bread")
        self.assertEqual(recipe.ingredients, {"Banana": 2, "Flour": 1, "Sugar": 1})
        self.assertEqual(recipe.expiration_date, datetime(2024, 12, 10))
        self.assertEqual(recipe.cooking_time, 60)
        self.assertEqual(
            recipe.nutritional_info,
            NutritionalInformation(
                total_kcal=200,
                total_fat=10,
                total_proteins=5,
                total_carbs=30,
                total_sugar=20,
            ),
        )


if __name__ == "__main__":
    unittest.main()
