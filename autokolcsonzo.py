
from datetime import date
from typing import List

from auto import Auto
from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev: str) -> None:
        if not nev:
            raise ValueError("A kölcsönző neve nem lehet üres.")
        self._nev = nev
        self._autok: List[Auto] = []
        self._berlesek: List[Berles] = []

    @property
    def nev(self) -> str:
        return self._nev

    @property
    def autok(self) -> List[Auto]:
        return list(self._autok)

    @property
    def berlesek(self) -> List[Berles]:
        return list(self._berlesek)

    def auto_hozzaadasa(self, auto: Auto) -> None:
        if not isinstance(auto, Auto):
            raise TypeError("Csak Auto példány adható hozzá.")
        if any(a.rendszam == auto.rendszam for a in self._autok):
            raise ValueError("Már létezik autó ezzel a rendszámmal.")
        self._autok.append(auto)

    def _auto_elerheto(self, auto: Auto, datum: date) -> bool:
        for berles in self._berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                return False
        return True

    def auto_berlese(self, auto_index: int, datum: date) -> int:
        if auto_index < 0 or auto_index >= len(self._autok):
            raise IndexError("Nincs autó a megadott indexen.")

        auto = self._autok[auto_index]

        if not self._auto_elerheto(auto, datum):
            raise ValueError("Az autó ezen a napon már foglalt.")

        uj_berles = Berles(auto, datum)
        self._berlesek.append(uj_berles)
        return auto.berleti_dij

    def berles_lemondasa_id_alapjan(self, berles_id: int) -> None:
        for berles in self._berlesek:
            if berles.id == berles_id:
                self._berlesek.remove(berles)
                return
        raise ValueError("Nincs ilyen azonosítójú bérlés.")

    def listaz_autok(self) -> None:
        if not self._autok:
            print("Nincs elérhető autó a kölcsönzőben.")
            return

        print(f"Autók a(z) {self.nev} kölcsönzőben:")
        for index, auto in enumerate(self._autok, start=1):
            print(f"{index}. {auto}")

    def listaz_berlesek(self) -> None:
        if not self._berlesek:
            print("Jelenleg nincs aktív bérlés.")
            return

        print("Aktív bérlések:")
        for berles in self._berlesek:
            print(berles)
