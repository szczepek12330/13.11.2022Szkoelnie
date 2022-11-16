#
# import pakiet.fundef
#
# print(pakiet.fundef.square(10))
# print(pakiet.fundef.cube(10))

import pakiet.fundef as p

a = p.square(10)
b = p.cube(10)
with open('test.log', 'w', encoding='utf-8') as f:
    f.write(str(a))
    f.write(str(b))

input("Wciśnij ENTER aby zakończyć...")


# from .first import godziny
# godziny.now

