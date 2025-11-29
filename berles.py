
from datetime import date
from auto import Auto


class Berles:
    _kovetkezo_id = 1

    def __init__(self, auto: Auto, datum: date) -> None:
        if not isinstance(auto, Auto):
            raise TypeError("A bérléshez egy Auto példány szükséges.")
        if not isinstance(datum, date):
            raise TypeError("A dátumnak datetime.date példánynak kell lennie.")
        if datum < date.today():
            raise ValueError("Múltbeli dátumra nem lehet bérlést létrehozni.")

        self._auto = auto
        self._datum = datum
        self._id = Berles._kovetkezo_id
        Berles._kovetkezo_id += 1

    @property
    def id(self) -> int:
        return self._id

    @property
    def auto(self) -> Auto:
        return self._auto

    @property
    def datum(self) -> date:
        return self._datum

    def __str__(self) -> str:
        return f"#{self.id} - {self.auto.rendszam} ({self.auto.tipus}) - {self.datum.isoformat()} - {self.auto.berleti_dij} Ft"

    def __repr__(self) -> str:
        return f"Berles(id={self.id!r}, auto={self.auto!r}, datum={self.datum!r})"
