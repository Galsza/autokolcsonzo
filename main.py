
from datetime import date

from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from utils import datum_bekerese


def inicializal_kolcsonzo() -> Autokolcsonzo:
    kolcsonzo = Autokolcsonzo("Minta Autókölcsönző")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 12000, 5)
    auto2 = Szemelyauto("DEF-456", "Volkswagen Golf", 13000, 5)
    auto3 = Teherauto("GHI-789", "Ford Transit", 20000, 1500)

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    # Előre felvett bérlések – jól olvasható, fix dátumokkal
    datum1 = date(2025, 12, 1)
    datum2 = date(2025, 12, 2)
    datum3 = date(2025, 12, 3)
    datum4 = date(2025, 12, 4)

    try:
        kolcsonzo.auto_berlese(0, datum1)
        kolcsonzo.auto_berlese(1, datum2)
        kolcsonzo.auto_berlese(2, datum3)
        kolcsonzo.auto_berlese(0, datum4)
    except Exception:
        pass

    return kolcsonzo


def beolvas_int(prompt: str, hibauzenet: str = "Hiba: egész számot adj meg.") -> int | None:
    try:
        return int(input(prompt))
    except ValueError:
        print(hibauzenet)
        return None


def auto_berlese(kolcsonzo: Autokolcsonzo) -> None:
    if not kolcsonzo.autok:
        print("Nincs elérhető autó.")
        return

    kolcsonzo.listaz_autok()
    sorszam = beolvas_int("Válaszd ki az autót (sorszám): ")
    if sorszam is None:
        return

    auto_index = sorszam - 1
    datum = datum_bekerese()

    try:
        ar = kolcsonzo.auto_berlese(auto_index, datum)
        print(f"Sikeres bérlés! A bérlés ára: {ar} Ft.")
    except Exception as e:
        print(f"Hiba a bérlés során: {e}")


def berles_lemondasa(kolcsonzo: Autokolcsonzo) -> None:
    if not kolcsonzo.berlesek:
        print("Nincs lemondható bérlés.")
        return

    kolcsonzo.listaz_berlesek()
    berles_id = beolvas_int("Add meg a lemondani kívánt bérlés azonosítóját: ")
    if berles_id is None:
        return

    try:
        kolcsonzo.berles_lemondasa_id_alapjan(berles_id)
        print("A bérlés sikeresen lemondva.")
    except Exception as e:
        print(f"Hiba: {e}")


def menu() -> None:
    print("\n--- Autókölcsönző Rendszer ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Autók listázása")
    print("0. Kilépés")


def felhasznaloi_felulet() -> None:
    kolcsonzo = inicializal_kolcsonzo()
    print(f"Üdvözöl a(z) {kolcsonzo.nev}!")

    while True:
        menu()
        valasztas = input("Választás: ")

        match valasztas:
            case "1":
                auto_berlese(kolcsonzo)
            case "2":
                berles_lemondasa(kolcsonzo)
            case "3":
                kolcsonzo.listaz_berlesek()
            case "4":
                kolcsonzo.listaz_autok()
            case "0":
                print("Kilépés a rendszerből. Viszlát!")
                break
            case _:
                print("Ismeretlen opció, próbáld újra.")


if __name__ == "__main__":
    felhasznaloi_felulet()
