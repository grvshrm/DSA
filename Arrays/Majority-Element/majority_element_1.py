# Majority Element - Element occuring more than n/2 times

def majorityElement(arr):
# Complexity : Time - O(n), Space - O(1)
# Moore's Voting Algorithm
	n = len(arr)
	cnt = 0
	elm = -1
	for i in range(n):
		if cnt == 0:
			cnt = 1
			elm = arr[i]
		elif arr[i] == elm:
			cnt += 1
		else:
			cnt -= 1
	cnt = 0
	for i in range(n):
		if arr[i] == elm:
			cnt += 1
	if cnt > n//2:
		return elm 
	return -1

"""from collections import defaultdict

def majorityElement(arr):
# Complexity : Time - O(n), Space - O(n)
	n = len(arr)
	map = defaultdict(int)
	for i in range(n):
		map[arr[i]] = map[arr[i]] + 1
	for item in map:
		if map[item] > n//2:
			return item
	return -1"""

if __name__ == "__main__":
	arr = [2, 2, 3, 3, 1, 2, 2]
	print(majorityElement(arr))