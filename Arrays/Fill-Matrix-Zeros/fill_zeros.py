def zeroFill(matrix, m, n):
# Complexity : Time - O(n*m ~ n^2), Space - O(1)
    col0 = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(m):
            matrix[i][0] = 0

"""def zeroFill(matrix, m, n):
# Complexity : Time - O(n*m ~ n^2), Space - O(n + m)
    rows = [1] * m
    cols = [1] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = 0
                cols[j] = 0
    for i in range(m):
        for j in range(n):
            if rows[i] == 0 or cols[j] == 0:
                matrix[i][j] = 0"""

"""def zeroFill(matrix, m, n):
# Complexity : Time - O(n^3), Space - O(1)
    col0 = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for x in range(m):
                    if matrix[x][j] != 0:
                        matrix[x][j] = -1
                for y in range(n):
                    if matrix[i][y] != 0:
                        matrix[i][y] = -1              
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0"""

def printMatrix(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()

if __name__ == '__main__':
    matrix = [[1, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 0, 1], 
              [0, 1, 1, 1]]
    m = len(matrix)
    n = len(matrix[0])
    print("Before Fill:")
    printMatrix(matrix, m, n)
    zeroFill(matrix, m, n)
    print("After Fill:")
    printMatrix(matrix, m, n)