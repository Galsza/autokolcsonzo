
from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras_kg: int) -> None:
        self._teherbiras_kg = None
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras_kg = teherbiras_kg


    @property
    def teherbiras_kg(self) -> int:
        return self._teherbiras_kg

    @teherbiras_kg.setter
    def teherbiras_kg(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("A teherbírásnak egész számnak kell lennie.")
        if value <= 0:
            raise ValueError("A teherbírás legyen pozitív.")
        self._teherbiras_kg = value

    def kategoria(self) -> str:
        return "Teherautó"

    def __str__(self) -> str:
        return super().__str__() + f", teherbírás: {self.teherbiras_kg} kg"
