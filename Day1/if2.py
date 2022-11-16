age = 120

if age > 90:
    print("Too old")
elif age < 0:
    print("Not yet be born")
elif age >= 18:
    print("party time")
else:
    "too young"

age = input("Wprowadź wiek")

match age:
    case "90":
        print("too old")
    case "18":
        print("party time")
    case "0":
        print("Not yet be born")
    case _:
        print(" :( ")