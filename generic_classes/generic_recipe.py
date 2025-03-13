from dataclasses import dataclass
from datetime import datetime
from generic_classes.nutritional_info import NutritionalInformation


@dataclass
class GenericRecipe:
    name: str
    ingredients: list
    expiration_date: datetime
    cooking_time: int
    nutritional_info: NutritionalInformation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def ingredients(self) -> list:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list) -> None:
        self._ingredients = ingredients

    @property
    def expiration_date(self) -> datetime:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime) -> None:
        self._expiration_date = expiration_date

    @property
    def cooking_time(self) -> int:
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time: int) -> None:
        self._cooking_time = cooking_time

    @property
    def nutritional_info(self) -> NutritionalInformation:
        return self._nutritional_info

    @nutritional_info.setter
    def nutritional_info(self, nutritional_info: NutritionalInformation) -> None:
        self._nutritional_info = nutritional_info

    def __str__(self) -> str:
        return f"Recipe name: {self._name}, ingredients: {self._ingredients}, expiration date: {self._expiration_date}, cooking time: {self._cooking_time}, nutritional information: {self._nutritional_info}."
