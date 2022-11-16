from functools import reduce

x = [1, 2, 3]


def func(x):
    x[1] = 42
    # x = 'bleble'


func(x)
print(x)


def pos(a, b, c):
    print(a, b, c)


values = (1, 3, -6)
val = {'a': 54, 'c': 55, 'b': 123}

pos(c=1, a=4, b="Tomek")
pos(*values)
pos(**val)


def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


# func(1, *(2, 3), f=6, *(4, 5))
# func(*(1, 2), e=5, *(3, 4), f=6)
# func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})
# func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f': 6})


def f1(a, b=34, c=4):
    print(a, b, c)


f1(b=5, a=6, c=7)


def minimum(*n):
    print(type(n))
    if n:
        mn = n[0]
        for val in n[1:]:
            if val < mn:
                mn = val
        print(mn)


minimum()
minimum(4, 6, 2, 43)
minimum(-5, 66, 3322)


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    print(options)


# connect()
# connect(port=9999, user='admin', pwd='12345')
# connect(port=9999, user='admin', pwd='12345', www='comarch.com')

def fun(a, b=2, /):
    print(a, b)


fun(4, 5)
fun(4)


def func_name(name, /, **kwargs):
    print(name)
    print(kwargs)


func_name('positional-only', name='Name in **kwargs')


def fun1(*a, c):
    print(a, c)


# fun1(1, 2, 3, c=4)
# fun1(c=4)


def fun2(a, b=42, *, c):
    print(a, b, c)


# fun2(3, b=7, c=99)
# fun2(3, c=99)
# fun2(3, 99)

# def fun3(a,b,c=3,*args,**kwargs)
#     print()

# new*
def func2(a=None, b=None):
    if b is None:
        b = {}
    if a is None:
        a = []


# new*
def nic():
    pass


# usuwamy elementy które sa bez sensu, małe funkcje, im mniej parametrów tym lepiej, spójnośc w zwracanych wartościach- liczba zwraca liczbe, tekst zwraca tekst


# new*
def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1)


# print(factorial(234))

def dodaj(a, b):
    return a + b


# new*
def to_upper(s):
    return s.upper()


print(dodaj(5, 5))
print(to_upper("Tomek"))
adder = lambda a, b: a + b
upper = lambda s: s.upper()
print(adder(5, 5))
print(upper('tomek'))

lista = [1, 3, 5, 7]

print(f"Zastosowanie map:{list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter:{list(filter(lambda x: x > 3, lista))}")
print(f"Zastosowanie reduce:{reduce(lambda x, y: x+ y, lista)}")
