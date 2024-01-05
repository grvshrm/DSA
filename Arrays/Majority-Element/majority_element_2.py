# Majority Element - Element occuring more than n/3 times

def majorityElement(arr):
# Complexity : Time - O(n), Space - O(1)
# Moore's Voting Algorithm
	n = len(arr)
	cnt1, cnt2 = 0, 0
	elm1, elm2 = -1, -1
	minimum = n//3 + 1
	ans = list()
	for i in range(n):
		if cnt1 == 0 and elm2 != arr[i]:
			cnt1 = 1
			elm1 = arr[i]
		elif cnt2 == 0 and elm1 != arr[i]:
			cnt2 = 1
			elm2 = arr[i]
		elif arr[i] == elm1:
			cnt1 += 1
		elif arr[i] == elm2:
			cnt2 += 1
		else:
			cnt1 -= 1
			cnt2 -= 1
	cnt1, cnt2 = 0, 0
	for i in range(n):
		if arr[i] == elm1:
			cnt1 += 1
		if arr[i] == elm2:
			cnt2 += 1
	if cnt1 >= minimum:
		ans.append(elm1)
	if cnt2 >= minimum:
		ans.append(elm2)	
	return ans

"""from collections import defaultdict

def majorityElement(arr):
# Complexity : Time - O(n), Space - O(n)
	n = len(arr)
	ans = list()
	map = defaultdict(int)
	minimum = n//3 + 1
	for i in range(n):
		map[arr[i]] = map[arr[i]] + 1
		if map[arr[i]] == minimum:
			ans.append(arr[i])
		if len(ans) == 2:
			break
	return ans"""

if __name__ == "__main__":
	arr = [2, 2, 3, 3, 1, 2, 3]
	print(majorityElement(arr))