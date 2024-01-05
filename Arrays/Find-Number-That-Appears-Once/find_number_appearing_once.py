def numAppearingOnce(arr):
# Complexity : Time - O(n), Space - O(1)
	num_xor = 0
	for i in arr:
		num_xor ^= i
	return num_xor

if __name__ == "__main__":
	arr = [1, 1, 2, 3, 3, 4, 4]
	print(numAppearingOnce(arr))