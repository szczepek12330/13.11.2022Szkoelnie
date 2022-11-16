# a = 10
#
# def dodawanie ():
#     global a
#     a = 5
#     b = 4
#     wynik = a + b
#     return wynik
#
#
# def odejmij():
#     b = 45
#     wynik = a-b
#     return wynik

# print(dodawanie())
# print(odejmij())
print(a)

#
# def outer():
#     test = 1
#     def inner():
#         test = 2
#         print('inner', test)
#     inner()
#     print('outer:', test)
#
# test = 0
#
#
# outer()
# print('global', test)

def outer():
    test = 1

    def inner():
        global test
        test = 2
        print('inner', test)
    inner()
    print('outer:', test)

test = 0

outer()
print('global', test)

