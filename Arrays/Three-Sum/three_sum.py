def tripletSum(arr, n):
# Complexity : Time - O(n^2), Space - O(1)
	ans = []
	arr.sort()
	for i in range(n):
		if i != 0 and arr[i] == arr[i-1]:
			continue
		j = i + 1
		k = n - 1
		while j < k:
			total_sum = arr[i] + arr[j] + arr[k]
			if total_sum < 0:
				j += 1
			elif total_sum > 0:
				k -= 1
			else:
				temp = [arr[i], arr[j], arr[k]]
				ans.append(temp)
				j += 1
				k -= 1
				while j < k and arr[j] == arr[j-1]:
					j += 1
				while j < k and arr[k] == arr[k+1]:
					k -= 1							
	return ans

"""def tripletSum(arr, n):
# Complexity : Time - O(n^2), Space - O(2 * No. of unique triplets)
	st = set()
	for i in range(n):
		hashSet = set()
		for j in range(i + 1, n):
			third = - (arr[i] + arr[j])
			if third in hashSet:
				temp = [arr[i], arr[j], third]
				temp.sort()
				st.add(tuple(temp))
			hashSet.add(arr[j])
	ans = [list(item) for item in st] #list(st) if Ok with Tuples
	return ans"""

"""def tripletSum(arr, n):
# Complexity : Time - O(n^3), Space - O(2 * No. of unique triplets)
	st = set()
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):
				if arr[i] + arr[j] + arr[k] == 0:
					st.add(tuple(sorted([arr[i], arr[j], arr[k]])))
	ans = [list(item) for item in st]
	return ans"""
		
if __name__ == "__main__":
	arr = [-1, 0, 1, 2, -1, -4]
	print(tripletSum(arr, len(arr)))