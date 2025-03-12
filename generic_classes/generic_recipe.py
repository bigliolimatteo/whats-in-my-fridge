from dataclasses import dataclass
from datetime import datetime
from generic_classes.generic_food import GenericFood


@dataclass
class GenericRecipe:
    name: str
    ingredients: GenericFood
    expiration_date: datetime
    cooking_time: int
    total_kcal: int

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def ingredients(self) -> GenericFood:
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, ingredients: GenericFood) -> None:
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
    def total_kcal(self) -> int:
        return self._total_kcal
    
    @total_kcal.setter
    def total_kcal(self, total_kcal: int) -> None:
        self._total_kcal = total_kcal
    
    def __str__(self) -> str:
        return f"Recipe name: {self._name}, ingredients: {self._ingredients}, expiration date: {self._expiration_date}, cooking time: {self._cooking_time}, total kcal: {self._total_kcal}"