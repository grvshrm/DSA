def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangleElement(row, col):
# Complexity : Time - O(r), Space - O(1)
    ans = nCr(row - 1, col - 1)
    return ans

if __name__ == "__main__":
    row = 5
    col = 3
    print(f"Element at ({row}, {col}) is: {pascalTriangleElement(row, col)}")