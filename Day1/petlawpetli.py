import operator
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# row = 5
# for i in range(1, 10, 2):
#     print(i)
#
# row = 5
# for i in range(1, row + 1):
#     for j in range(i):
#         print(j + 1, end= " ")
#     print()
#
# row= 5
# for i in range(row, 0, -1):
#      for j in range(i,0,-1):
#          print(j, end=" ")
#      print()
#
# row = 5
# maxCol = 5
# for i in range(0, row +1):
#     for j in range(maxCol - i, 0, -1):
#         print(j, end=" ")
#     print()

# # start = input() || x
# # end = input() || x
# # Wypisać wszystkie liczby pierwze od 1 do zadanej liczby
# range
# start = 25
# end = 50
# Wyniki
# 29
# 31
# 37
# 41
# 43
# 47

# def isPrime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True;
#
#
# start = int(input("Podaj Liczbe start "))
# end = int(input("Podaj Liczbe end "))
#
# for i in range(start, end + 1):
#     if (isPrime(i)):
#         print(i);

# start = 25
# end = 50
#
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#
# start = 25
# end = 50
#
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]

wynik = list(map(operator.add, list1, list2))
print(wynik)