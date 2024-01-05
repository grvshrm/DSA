def maxLen(arr, k):
# Complexity : Time - O(n), Space - O(1). Doesn't Work for negatives
	left, right = 0, 0
	max_len = 0
	curr_sum = arr[0]
	n = len(arr)
	while right < n:
		while left <= right and curr_sum > k:
			curr_sum -= arr[left]
			left += 1
		if curr_sum == k:
			max_len = max(max_len, right - left + 1)
		right += 1
		if right < n:
			curr_sum += arr[right]
	return max_len

"""def maxLen(arr, k):
# Complexity : Time - O(n), Space - O(n). Works for negatives
	hash_map = {}
	max_len = 0
	curr_sum = 0
	for i in range(len(arr)):
		curr_sum += arr[i]
		if curr_sum == k:
			max_len = i + 1
		if curr_sum - k in hash_map:
			max_len = max(max_len, i - hash_map[curr_sum - k])
		if curr_sum not in hash_map:
			hash_map[curr_sum] = i
	return max_len"""

"""def maxLen(arr, k):
# Complexity : Time - O(n^2), Space - O(1)
	max_len = 0
	for i in range(len(arr)):
		curr_sum = 0
		for j in range(i, len(arr)):
			curr_sum += arr[j]
			if curr_sum == k:
				max_len = max(max_len, j-i + 1)
	return max_len"""

if __name__ == "__main__":
	arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
	k = 6
	print(f"Length of the longest {k} sum subarray is {maxLen(arr, k)}")