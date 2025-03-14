from dataclasses import dataclass


@dataclass
class NutritionalInformation:
    total_kcal: int
    total_fat: int
    total_proteins: int
    total_carbs: int
    total_sugar: int

    def __str__(self) -> str:
        return f"Total kcal: {self._total_kcal}, total fat: {self._total_fat}, total proteins: {self._total_proteins}, total carbs: {self._total_carbs}, total sugar: {self._total_sugar}."
