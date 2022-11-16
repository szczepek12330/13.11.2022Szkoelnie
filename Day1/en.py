from enum import Enum


class Rozmiar(Enum):
    S = 1
    M = 2
    L = 3
    XL = 4

print(Rozmiar.S.name)
print(Rozmiar.S.value)
print(Rozmiar(1))
print(Rozmiar(2))
print(Rozmiar(3))
print(Rozmiar(4))



ROZMIARY = ('S', 'M', 'L', 'XL')


