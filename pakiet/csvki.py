# import csv
#
# filename = "Sample.csv"
# fields = []
# rows = []
#
# with open(filename, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fields = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
#     print(f"Total no of rows: {csvreader.line_num}")
# print('Field names are:' + ','.join(field for field in fields))
#
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     for col in row:
#         print("%10s" % col, end=" ")
#     print('\n')

fields = ['name', 'branch', 'year', 'cgpa']

# data rows of csv file
# rows = [['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
# with open('records.csv', 'w') as csvf:
#     csvwriter = csvf.writer(csvf)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(row)

mydict =[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]

with open('records_dict.csv', 'w') as csvf:
    csvwriter = csvf.DictWriter(csvf, fieldnames=fields)

    csvwriter.writeheader()
    csvwriter.writerows(mydict)


