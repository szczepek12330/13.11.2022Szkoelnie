# slownik = {}
# slownik[1] = "Tomek"
# slownik[2] = "Tomek2"
# slownik[3] = "Tomek3"
# slownik['imie'] = "Kasia"
# slownik[3] = "Łukasz"
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
# slownik.pop(1)
# print(slownik['imie'])
# print(slownik)
# print(slownik.get('imie'))
# print(slownik.get('imie2'))

customers = [
    dict(id=1, total=2000, code=43333),
    dict(id=2, total=3000, code=543333),
    dict(id=3, total=4000, code=643333)
]

for customer in customers:
    print(customer['id'], customer['total'], customer['code'])

# print(customers[0])
wynik = customers[0]['total']
print(wynik)