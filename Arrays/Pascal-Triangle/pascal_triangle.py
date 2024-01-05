def generateRow(row):
    ans = 1
    ansRow = [ans]
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n):
# Complexity : Time - O(n^2), Space - O(1)  
    ansTriangle = list()
    for i in range(1, n + 1):
        ansTriangle.append(generateRow(i))
    return ansTriangle

"""def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n):
# Complexity : Time - O(n^3), Space - O(1)
    ans = []
    for row in range(1, n + 1):
        tempLst = []
        for col in range(1, row + 1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans"""

if __name__ == "__main__":
    n = 6
    ans = pascalTriangle(n)
    for row in ans:
        for ele in row:
            print(ele, end = " ")
        print()