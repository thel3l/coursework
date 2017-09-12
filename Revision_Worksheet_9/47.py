def generate2DArray(array1D):
    n = len(array1D)
    array2D = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if(j<n-i):
                array2D[i][j] = array1D[j]
            else:
                array2D[i][j] = 0
    return array2D

def matrixToString(matrix):
    for row in matrix:
        print ' '.join(map(str,row))

def PrintPattern(Num):
    matrix = generate2DArray(Num)
    string = matrixToString(matrix)
    print string

a = PrintPattern([1,2,3,4])
b = PrintPattern([12, 32, 43, 54, 46, 57])