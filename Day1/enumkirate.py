from enum import Enum


class Pora(Enum):
    WIOSNA = 'wiosna'
    LATO = 'lato'
    JESIEN = 'jesień'
    ZIMA = 'zima'


# TODO zweryfikować
# pora = input("Podaj porę roku: ")
pora = 'wiosna'

match pora:
    case Pora.WIOSNA:
        print("1")
    case Pora.LATO:
        print("2")
    case Pora.JESIEN:
        print("3")
    case Pora.ZIMA:
        print("4")
    case _:
        print("Błędna wartość pory roku")

pory_roku = enumerate(['wiosna', 'lato', 'jesień', 'zima'])
