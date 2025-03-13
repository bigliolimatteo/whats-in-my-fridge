from dataclasses import dataclass


@dataclass
class NutritionalInformation:
    total_kcal: int
    total_fat: int
    total_proteins: int
    total_carbs: int
    total_sugar: int

    @property
    def total_kcal(self) -> int:
        return self._total_kcal

    @total_kcal.setter
    def total_kcal(self, total_kcal: int) -> None:
        self._total_kcal = total_kcal

    @property
    def total_fat(self) -> int:
        return self._total_fat

    @total_fat.setter
    def total_fat(self, total_fat: int) -> None:
        self._total_fat = total_fat

    @property
    def total_proteins(self) -> int:
        return self._total_proteins

    @total_proteins.setter
    def total_proteins(self, total_proteins: int) -> None:
        self._total_proteins = total_proteins

    @property
    def total_carbs(self) -> int:
        return self._total_carbs

    @total_carbs.setter
    def total_carbs(self, total_carbs: int) -> None:
        self._total_carbs = total_carbs

    @property
    def total_sugar(self) -> int:
        return self._total_sugar

    @total_sugar.setter
    def total_sugar(self, total_sugar: int) -> None:
        self._total_sugar = total_sugar

    def __str__(self) -> str:
        return f"Total kcal: {self._total_kcal}, total fat: {self._total_fat}, total proteins: {self._total_proteins}, total carbs: {self._total_carbs}, total sugar: {self._total_sugar}."
