def maxOnes(arr):
# Complexity : Time - O(n), Space - O(1)
	max1 = 0
	cnt = 0
	for i in range(len(arr)):
		if arr[i] == 1:
			cnt += 1
			max1 = max(max1, cnt)
		else:
			cnt = 0
	return max1

if __name__ == "__main__":
	arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
	print(maxOnes(arr))