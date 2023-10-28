def is_arr_equal(arr1, arr2):
# Complexity : Time - O(n), Space - O(n)
	if len(arr1) != len(arr2):
		return False
	count = {}
	for i in arr1:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	for i in arr2:
		if i not in count or count[i] == 0:
			return False
		else:
			count[i] -= 1
	return True

"""
def areEqual(arr1, arr2, N, M):
# Complexity : Time - O(n*logn), Space - O(1)
    if (N != M):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0, N):
        if (arr1[i] != arr2[i]):
            return False
    return True
 
"""

if __name__ == "__main__":
	arr1 = [3, 5, 2, 5, 2]
	arr2 = [2, 3, 5, 5, 2]

	if is_arr_equal(arr1, arr2):
		print("Yes")
	else:
		print("No")