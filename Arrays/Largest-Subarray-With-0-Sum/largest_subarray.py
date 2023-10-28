def maxLen(arr):
# Complexity : Time - O(n), Space - O(n)
    hash_map = {}
    max_len = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
    return max_len

"""def maxLen(arr):
# Complexity : Time - O(n^2), Space - O(1)
	max_len = 0
	for i in range(len(arr)):
		curr_sum = 0
		for j in range(i, len(arr)):
			curr_sum += arr[j]
			if curr_sum == 0:
				max_len = max(max_len, j-i + 1)
	return max_len"""

if __name__ == "__main__":
	arr = [15, -2, 2, -8, 1, 7, 10, 13]
	print ("Length of the longest 0 sum subarray is % d" % maxLen(arr))
