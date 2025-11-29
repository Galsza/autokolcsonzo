
from abc import ABC, abstractmethod

class Auto(ABC):

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int) -> None:
        self._rendszam = None
        self._tipus = None
        self._berleti_dij = None

        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @property
    def rendszam(self) -> str:
        return self._rendszam

    @rendszam.setter
    def rendszam(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("A rendszámnak szövegnek kell lennie.")
        if not value:
            raise ValueError("A rendszám nem lehet üres.")
        self._rendszam = value.upper()

    @property
    def tipus(self) -> str:
        return self._tipus

    @tipus.setter
    def tipus(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("A típusnak szövegnek kell lennie.")
        if not value:
            raise ValueError("A típus nem lehet üres.")
        self._tipus = value

    @property
    def berleti_dij(self) -> int:
        return self._berleti_dij

    @berleti_dij.setter
    def berleti_dij(self, value: int) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("A bérleti díjnak számnak kell lennie.")
        if value <= 0:
            raise ValueError("A bérleti díjnak pozitívnak kell lennie.")
        self._berleti_dij = int(value)

    @abstractmethod
    def kategoria(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.kategoria()} - {self.rendszam} ({self.tipus}), {self.berleti_dij} Ft/nap"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(rendszam={self.rendszam!r}, tipus={self.tipus!r}, berleti_dij={self.berleti_dij!r})"
