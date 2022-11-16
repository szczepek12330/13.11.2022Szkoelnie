'''
# Napisz funkcje, która przyjmuje dwie macierze i zwraca jedną macierz, która jest sumą dwóch podanaych w argumentach
# Suma macierzy to suma ich elementów na konkretnych pozycjach: [1, 2] + [5, 6] = [6, 8]
11 12 13
21 22 23
31 32 33
'''

def createMatrix(rows, cols, begin=1, step=1):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(begin)
            begin += 1 * step
        matrix.append(row)
    return matrix
matrix1 = createMatrix(4, 2, 3)
matrix2 = createMatrix(4, 2, 10, -2)
printMatrix(
    sumMatrix(
        matrix1,
        matrix2,
    )
)

def printMatrix(matrix):
    if matrix is None:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end="\t")

            def matrixCalculator(matrix1, matrix2, operator='+'):
                if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                    print("Macierze nie mają tych samych rozmiarów")
                    return

                outputList = []
                for row in range(0, len(matrix1)):
                    newlist = []
                    for col in range(0, len(matrix1[0])):
                        match operator:
                            case '+':
                                newlist.append(matrix1[row][col] + matrix2[row][col])
                            case '-':
                                newlist.append(matrix1[row][col] - matrix2[row][col])
                            case '*':
                                newlist.append(matrix1[row][col] * matrix2[row][col])
                            case '/':
                                newlist.append(matrix1[row][col] / matrix2[row][col])
                            case _:
                                print("Błędny operator matematyczny")
                                return
                    outputList.append(newlist)
                return outputList


