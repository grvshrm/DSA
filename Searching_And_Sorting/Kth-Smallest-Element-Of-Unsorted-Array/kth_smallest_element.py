def count(nums, mid):
	cnt = 0
	for i in range(len(nums)):
		if nums[i] <= mid:
			cnt += 1
	return cnt

def kthSmallest(nums, k):
# Complexity : Time - O(n*(log(n))), Space - O(1)
	low = float('inf')
	high = float('-inf')
	for i in range(len(nums)):
		low = min(low, nums[i])
		high = max(high, nums[i])
	while low < high:
		mid = low + (high - low) // 2
		if count(nums, mid) < k:
			low = mid + 1
		else:
			high = mid
	return low

if __name__ == "__main__":
	nums = [1, 4, 5, 3, 19, 3]
	k = 3
	print("K'th smallest element is", kthSmallest(nums, k))