from abc import ABC, abstractmethod


class ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "startuje i osiągne prędkość:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass

class Orzel(ptak):

    def poluj(self):
        print("Tu", self.gatunek, "poluje...")
    def wydajOdglos(self):
        print("piiii")

class Kura(ptak):

    def __init__(self, gatunek='ptactwo'):
        super().__init__(gatunek, 0)
    def lataj(self):
        print("Ja nie latam!")
    def wydajOdglos(self):
        print("kokokoko")