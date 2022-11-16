def createMatrix(rows, cols):
    matrix = []
    iter = 1
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(iter)
            iter += 1
        matrix.append(row)
    printMatrix(matrix, cols, rows)
    return matrix

def printMatrix(matrix, cols, rows):
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end="\t")
        print()


matrix = createMatrix(3, 4)
printMatrix(matrix, 3, 4)
