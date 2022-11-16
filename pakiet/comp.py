squares = []
for n in range(10):
    squares.append(n ** 2)

print(squares)

print(list(map(lambda n: n**2, range(10))))

squares = [n ** 2 for n in range(10)]
print(squares)

items = 'ABCD'
pairs = [(items[a], items[b])
    for a in range(len(items)) for b in range(a, len(items))]
print(pairs)

slownik = {1: "Tomek", 2:"Jakub", 3: "Łukasz"}
print({value: key for key, value in slownik.items()})

