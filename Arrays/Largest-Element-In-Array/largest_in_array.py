def largestElement(arr):
# Complexity : Time - O(n), Space - O(1)
	lar = arr[0]
	for i in range(1, len(arr)):
		if(arr[i] > lar):
			lar = arr[i]
	return lar

if __name__ == "__main__":
	arr = [3, 2, 1, 6, 5, 2]
	print(largestElement(arr))