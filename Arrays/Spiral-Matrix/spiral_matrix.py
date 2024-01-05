def spiralMatrix(matrix, m, n):
# Complexity : Time - O(n*m ~ n^2), Space - O(n*m ~ n^2)
    left, top = 0, 0
    right, bottom = n - 1, m - 1
    ans = list()
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1    
    return ans 

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12], 
              [13, 14, 15, 16]]
    m = len(matrix)
    n = len(matrix[0])
    print("Spiral Matrix:")
    print(spiralMatrix(matrix, m, n))