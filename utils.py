
from datetime import date


def datum_bekerese() -> date:
    while True:
        datum_str = input("Add meg a bérlés napját (YYYY-MM-DD): ")
        try:
            datum = date.fromisoformat(datum_str)
        except ValueError:
            print("Hibás dátumformátum. Példa: 2025-11-30")
            continue

        if datum < date.today():
            print("Múltbeli dátumra nem lehet bérlést felvenni.")
            continue

        return datum
