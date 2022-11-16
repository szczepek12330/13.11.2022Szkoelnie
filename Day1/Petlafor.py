count = 1
list = []
while count < 10:
    list.append(count)
    count += 1
print(list)




for i in list:
    if i % 2 != 0:
        continue
    if i == 8:
        pass
    print(i, end=" ")
else:
    print("\n Koniec")