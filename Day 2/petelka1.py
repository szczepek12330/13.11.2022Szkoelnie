# for i in [0, 1, 2, 3, 4]:
#     print(i * 21)
#
# for i in range(1, 9, 2):
#     print(i)


surnames = ['Rivest', 'Shamir', 'Adleman']

# for pos in range(len(surnames)):
#     print(pos, surnames[pos])

# for pos, sur in enumerate(surnames): #bateryjka
#     print(pos, sur)

people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 22]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']


# for pos, per in enumerate(people):
#     age = ages[pos]
#     print(per, age)

# for per, age, ins in zip(people, ages, instruments):
#     print(per, age, ins)

for p in people:
    print(p)
    for i in ages:
            print(i)
