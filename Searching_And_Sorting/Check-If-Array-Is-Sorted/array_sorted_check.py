def sortedCheck(arr):
# Complexity : Time - O(n), Space - O(1)
	for i in range(1, len(arr)):
		if(arr[i] < arr[i-1]):
			return False
	return True

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	print(sortedCheck(arr))