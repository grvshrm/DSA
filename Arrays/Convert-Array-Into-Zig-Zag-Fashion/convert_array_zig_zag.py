def zigZag(arr, n):
# Complexity : Time - O(n), Space - O(1)
    flag = True
    for i in range(n-1):
        # "<" relation expected
        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # ">" relation expected
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1 - flag)
    print(arr)

if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    zigZag(arr, n)