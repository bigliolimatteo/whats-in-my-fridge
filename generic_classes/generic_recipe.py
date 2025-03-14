from dataclasses import dataclass
from datetime import datetime
from generic_classes.nutritional_info import NutritionalInformation
from generic_classes.generic_food import GenericFood

@dataclass
class GenericRecipe:
    name: str
    ingredients: list[GenericFood]
    expiration_date: datetime
    cooking_time: int
    nutritional_info: NutritionalInformation

    def __str__(self) -> str:
        return f"Recipe name: {self._name}, ingredients: {self._ingredients}, expiration date: {self._expiration_date}, cooking time: {self._cooking_time}, nutritional information: {self._nutritional_info}."
