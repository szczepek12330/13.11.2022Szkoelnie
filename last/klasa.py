class Human:
    imie = ""
    wiek = None
    plec = ""

    def przywitaj(self):
        print("Cześć, mam na imię:", self.imie)

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