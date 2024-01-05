def twoSum(arr, target):
# Complexity : Time - O(n*log(n)), Space - O(1)
	n = len(arr)
	arr.sort()
	sumFound = False
	i, j = 0, n-1
	while i < j:
		sum = arr[i] + arr[j]
		if sum == target:
			sumFound = True
			print("Yes")
			break
		elif sum < target:
			i += 1
		else:
			j -= 1
	if not sumFound:
		print("Not Found")

"""def twoSum(arr, target):
# Complexity : Time - O(n), Space - O(n)
	n = len(arr)
	hashMap = dict()
	sumFound = False
	for i in range(n):
		val = arr[i]
		more = target - val
		if more in hashMap:
			sumFound = True
			print(f"Sum found between indexes : {hashMap[more]} and {i}")
			break
		else:
			hashMap[val] = i
	if not sumFound:
		print("Not Found")"""

"""def twoSum(arr, target):
# Complexity : Time - O(n^2), Space - O(1)
	n = len(arr)
	sumFound = False
	for i in range(n):
		for j in range(i+1, n):
			if arr[i] + arr[j] == target:
				sumFound = True
				print(f"Sum found between indexes : {i} and {j}")
				break
	if not sumFound:
		print("Not Found")"""

if __name__ == "__main__":
	arr = [2, 6, 5, 8, 11]
	target = 14
	twoSum(arr, target)