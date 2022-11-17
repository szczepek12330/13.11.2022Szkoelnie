import random


class Human2:

    def __init__(self, imie, wiek, plec):
        self.__imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Ja sobie wylosuje zaraz imię...")
        self.__setImie()
        print("Cześć, mam na imię:", self.__imie)

    def spacer(self):
        if self.plec == 'k':
            print("Ruszyłam na spacer")
        else:
            print("Ruszyłem na spacer")

    def dodaj(self):
        if self.wiek < 2:
            print("Dopiero się uczę")
        else:
            print("Ok!")

    def __setImie(self):
        imiona = ["Tomek", "Piotr", "Damian"]
        self.__imie = random.choice(imiona)
        print("Nowe imię:", self.__imie)