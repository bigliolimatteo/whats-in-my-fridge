from dataclasses import dataclass


@dataclass
class NutritionalInformation:
    total_kcal: int
    total_fat: int
    total_proteins: int
    total_carbs: int
    total_sugar: int

    def __str__(self) -> str:
        return f"Total kcal: {self.total_kcal}, total fat: {self.total_fat}, total proteins: {self.total_proteins}, total carbs: {self.total_carbs}, total sugar: {self.total_sugar}."
