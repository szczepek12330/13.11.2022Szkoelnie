'''
1 2 3
4 5 6
7 8 9

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''

cols = 3
rows = 5

matrix = []
iter = 1
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(iter)
        iter += 1
    matrix.append(row)

for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end="\t")
    print()