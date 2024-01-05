def fourSum(arr, n):
# Complexity : Time - O(n^3), Space - O(2 * No. of unique triplets)
	st = set()
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):
				if arr[i] + arr[j] + arr[k] == 0:
					st.add(tuple(sorted([arr[i], arr[j], arr[k]])))
	ans = [list(item) for item in st]
	return ans
		
if __name__ == "__main__":
	arr = [1, 0, -1, -2, -2, -0]
	print(fourSum(arr, len(arr)))