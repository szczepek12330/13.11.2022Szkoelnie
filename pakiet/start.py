# #
# # import pakiet.fundef
# #
# # print(pakiet.fundef.square(10))
# # print(pakiet.fundef.cube(10))
#
# import pakiet.fundef as p
#
# a = p.square(10)
# b = p.cube(10)
# with open('test.log', 'w', encoding='utf-8') as f:
#     f.write(str(a))
#     f.write(str(b))
#
# input("Wciśnij ENTER aby zakończyć...")


# from .first import godziny
# godziny.now


# from last.klasa import Human
# from last.klasa2 import Human2
#
# adam = Human()
# adam.imie = "Adam"
# adam.wiek = 25
# adam.plec = "m"
# print(adam)
# adam.przywitaj()
# adam.spacer()
# adam.dodaj()
#
# ewa = Human()
# ewa.imie = "Ewa"
# ewa.wiek = 35
# ewa.plec = "k"
# ewa.przywitaj()
# ewa.spacer()
# ewa.dodaj()
#
# jakub = Human2(plec="m", wiek=30, imie="Jakub")
# jakub.przywitaj()
# jakub.spacer()
#
# michal = Human2(plec="m", wiek=11, imie="Michał")
# michal.przywitaj()

from last import ptak

bielik = ptak.Orzel("orzeł", 100)
bielik.lataj()
bielik.poluj()
bielik.wydajOdglos()
kura = ptak.Kura("kura")
kura.lataj()
kura.wydajOdglos()
