# from pascal_triangle_element import nCr

def pascalTriangleRow(n):
# Complexity : Time - O(n), Space - O(1)
    ans = 1
    print(ans, end = " ")
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end = " ")
    print()

"""def pascalTriangleRow(n):
# Complexity : Time - O(n * r), Space - O(1)
    for c in range(1, n + 1):
        print(nCr(n - 1, c - 1), end = " ")
    print()"""

if __name__ == "__main__":
    n = 6
    pascalTriangleRow(n)