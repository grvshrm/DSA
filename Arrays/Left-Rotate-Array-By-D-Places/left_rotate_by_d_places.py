def rotateList(arr, start, end):
	while(start <= end):
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

def leftRotateByD(arr, n, d):
# Complexity : Time - O(n + d), Space - O(1)
	d %= n
	rotateList(arr, 0, d - 1)
	rotateList(arr, d, n - 1)
	rotateList(arr, 0, n - 1)
	return arr

"""def leftRotateByD(arr, n, d):
# Complexity : Time - O(n + d), Space - O(d)
	d %= n
	temp = arr[:d]
	for i in range(d, n):
		arr[i - d] = arr[i]
	for i in range(n-d, n):
		arr[i] = temp[i - (n-d)]
	return arr"""

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	d = 3
	print(leftRotateByD(arr, len(arr), d))