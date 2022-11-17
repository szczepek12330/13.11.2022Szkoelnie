def multi(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        print("Niedozwolona operacja")
        return 0

def add(a,b):
    try:
        return a / b
    except Exception as e:
        print("Wystąpił:", e)
        return 0

add(6, 0)


valid_data = [{'name': 'Jan', 'age': '10'},
              {'name': 'Dawid', 'age': '25'},
              {'name': 'Marcin', 'age': '23'}]

invalid_data2 = [{'name': 'Jan', 'age': 'age'},
                 {'name': 'Dawid', 'age': '25'},
                 {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except KeyError:
            print(f"Niepoprawne dane: {user}")
        except ValueError:
            print(f"Niepoprawny wiek: {user}")
    return count

def check_age2(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print(f"Niepoprawne dane: {user}")
        except ValueError:
            print(f"Niepoprawny wiek: {user}")
        else:
            count += 1 if user_age < age else 0
        finally:
            print(f"{i}, {user}")
    return count

# print(check_age(valid_data, 15))
# print(check_age(invalid_data2, 15))
# print(check_age(invalid_data2, 15))
print(check_age2(invalid_data2, 15))
print(check_age2(valid_data, 15))
# print(multi('a', 'b'))
# print(multi('a', 5))
