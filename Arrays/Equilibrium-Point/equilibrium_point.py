def findElement(arr, size) :
# Complexity : Time - O(n), Space - O(1)
    right_sum, left_sum = 0, 0
    for i in range(1, size) :
        right_sum += arr[i]
    i, j = 0, 1
    while j < size :
        right_sum -= arr[j]
        left_sum += arr[i]
        if left_sum == right_sum :
            return arr[i + 1]
        j += 1
        i += 1
    return -1
"""
# Complexity : Time - O(n^2), Space - O(1)
def findElement(arr, n):
	for i in range(1, n):
		leftSum = sum(arr[0:i])
		rightSum = sum(arr[i+1:])
		if(leftSum == rightSum):
			return arr[i]
	return -1
"""

if __name__ == "__main__":

	# Case 1
	arr = [1, 4, 2, 5]
	n = len(arr)
	print(findElement(arr, n))

	# Case 2
	arr = [2, 3, 4, 1, 4, 5]
	n = len(arr)
	print(findElement(arr, n))