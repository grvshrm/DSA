def rightRotate(matrix, m, n):
# Complexity : Time - O(n^2), Space - O(1)
    for i in range(m):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(m):
        matrix[i].reverse()
    return matrix

"""def rightRotate(matrix, m, n):
# Complexity : Time - O(n^2), Space - O(n^2)
    ans = [[0 for _ in range(n)] for _ in range(m)] #[[0] * n] * m
    for i in range(m):
        for j in range(n):
            ans[j][n - i - 1] = matrix[i][j]
    return ans"""

def printMatrix(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12], 
              [13, 14, 15, 16]]
    m = len(matrix)
    n = len(matrix[0])
    print("Before Rotation:")
    printMatrix(matrix, m, n)
    print("After Rotation:")
    ans = rightRotate(matrix, m, n)
    printMatrix(ans, m, n)