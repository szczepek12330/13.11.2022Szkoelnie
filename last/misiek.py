import pandas as pd

# dane = pd.read_excel('imiona.xlsx', sheet_name='Wynik', header=1)
# dane2 = pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names=['Imie', 'Nazwisko', 'Wynik'])
miasta = pd.read_csv('miasta.csv')
# print(dane2[2:5])
# print(miasta.tail())
# print(miasta.tail()[['city', 'id']])
# print(miasta.id.is_unique)
miasta.set_index('id', inplace=True)
miasta.loc[1392685764, 'capital'] = 'secondary'
print((miasta['city'] == 'Tokyo') | (miasta['city'] == 'Jakarta'))
miasta['Nowa'] = '0'
miasta.loc[miasta['city'] == 'Tokyo', 'Nowa'] = 1
print(miasta)
# print(dane2.head())
# print(dane2[['Imie', 'Wynik']])
# print(dane2.Imie, dane2.Wynik)
# print(dane2.info())
# print(miasta.id.describe())
# print(miasta.isnull().sum())
# print(miasta.duplicated().sum())
# miasta.drop_duplicates()



# lista = [[13, 5, 7, 9], [11, 22, 33, 44]]
# slownik = {'Imię': ['Ania', 'Michał', 'Przemek'], 'wiek': [13, 23, 44]}
# zbior = pd.DataFrame(lista)
# zbior2 = pd.DataFrame(slownik)
# zbior.columns = ['jeden', 'dwa', 'trzy', 'czwartek']
# print(zbior2)
# zbior2.to_json('nowy.json')







# lista = [[13, 5, 7, 9], [11, 22, 33, 44]]
# slownik = {'Imię':['Ania', 'Michał', 'Przemek'], 'wiek': [13, 23, 44]}
# zbior = pd.DataFrame(lista)
# zbior2 = pd.DataFrame(slownik)
# zbior.columns = ['jeden', 'dwa', 'trzy', 'cztery']
# print(zbior2)
miasta.to_excel('test2.xls')