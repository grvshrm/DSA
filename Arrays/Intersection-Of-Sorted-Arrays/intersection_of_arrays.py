def intersection(arr1, arr2):
# Complexity : Time - O(n1 + n2), Space - O(1s)
	n1 = len(arr1)
	n2 = len(arr2)
	i, j = 0, 0
	intersectionList = list()
	while(i < n1 and j < n2):
		if arr1[i] < arr2[j]:
			i += 1
		if arr2[j] < arr1[i]:
			j += 1
		else:
			intersectionList.append(arr1[i])
			i += 1
			j += 1	
	return intersectionList

if __name__ == "__main__":
	arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
	arr2 = [2, 3, 3, 5, 6, 6, 7]
	print(intersection(arr1, arr2))