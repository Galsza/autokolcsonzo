
from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ulesek_szama: int) -> None:
        self._ulesek_szama = None
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    @property
    def ulesek_szama(self) -> int:
        return self._ulesek_szama

    @ulesek_szama.setter
    def ulesek_szama(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Az ülések számának egész számnak kell lennie.")
        if value <= 0:
            raise ValueError("Az ülések száma legyen pozitív.")
        self._ulesek_szama = value

    def kategoria(self) -> str:
        return "Személyautó"

    def __str__(self) -> str:
        return super().__str__() + f", ülések száma: {self.ulesek_szama}"
