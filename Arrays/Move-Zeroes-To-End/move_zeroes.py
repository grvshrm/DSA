def moveZeroes(arr, n):
# Complexity : Time - O(n), Space - O(1)
	j = -1
	for i in range(n):
		if(arr[i] == 0):
			j = i
			break
	if j == -1:
		return arr
	for i in range(j + 1, n):
		if arr[i] != 0:
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
	return arr

"""def moveZeroes(arr, n):
# Complexity : Time - O(2n), Space - O(x), x is no. of Non-Zero numbers
	temp = list()
	for i in range(n):
		if(arr[i] != 0):
			temp.append(arr[i])
	for i in range(len(temp)):
		arr[i] = temp[i]
	for i in range(len(temp), n):
		arr[i] = 0
	return arr"""

if __name__ == "__main__":
	arr = [0, 1, 0, 2, 3, 0, 4, 5]
	print(moveZeroes(arr, len(arr)))