import sqlite3

conn = sqlite3.connect('dane.sqlite')

c = conn.cursor()

# c.execute('''
#             CREATE TABLE transakcje
#             (data TEXT, id INTEGER,cena REAL)''')

# c.execute('''
#             INSERT INTO transakcje VALUES
#             ('2022-11-17',11,17.50)
# ''')
# c.execute('''
#             INSERT INTO transakcje VALUES
#             ('2022-11-16',19,123.50)
# ''')
# lista2 = ('2022-11-13', 13, 1233.20)
# c.execute(f'''
#             INSERT INTO transakcje VALUES
#             {lista2}
# ''')

# lista = []
#
# for row in c.execute('SELECT * FROM transakcje ORDER BY cena'):
#     print(row)
#     lista.append(row)

conn.commit()
conn.close()
# print(lista)


