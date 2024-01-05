def leftRotateByOne(arr, n):
# Complexity : Time - O(n), Space - O(1)
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	print(leftRotateByOne(arr, len(arr)))