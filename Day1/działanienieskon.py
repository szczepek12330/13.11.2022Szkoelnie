'''
count() - pozwala iterować od wartości początkowej do inf, opcjonalnie co krok inny niż 1
itertools.count(start, opt_krok)

cycle() - pozwala w nieskończoność iterować po zbiorze danych
itertools.cycle(iterator)

repeat() - pozwala w nieskończoność iterować po jednej wartości (opcjonalnie opt_times razy)
itertools.repeat(obj, opt_times)
'''
import itertools

print("Count")
for i in itertools.count(2, 2):
    if i > 100:
        break
    print(i, end=" ")

print()
print("Cycle")
licznik = 0
for i in itertools.cycle("Ala ma kota. "):
    print(i, end="")
    licznik += 1
    if licznik == 100:
        break

print()
print("Repeat 1")
for i in itertools.repeat(20):
    if licznik == 110:
        break
    print(i, end=" ")
    licznik += 1

print()
print("Repeat 2")
print(
    list(itertools.repeat(20, 6)), ".", sep=""
)
