def union(arr1, arr2):
# Complexity : Time - O(n1 + n2), Space - O(n1 + n2)
	n1 = len(arr1)
	n2 = len(arr2)
	i, j = 0, 0
	unionList = list()
	while(i < n1 and j < n2):
		if arr1[i] <= arr2[j]:
			if len(unionList) == 0 or unionList[-1] != arr1[i]:
				unionList.append(arr1[i])
			i += 1
		else:
			if len(unionList) == 0 or unionList[-1] != arr2[j]:
				unionList.append(arr2[j])
			j += 1
	while(j < n2):
		if len(unionList) == 0 or unionList[-1] != arr2[j]:
			unionList.append(arr2[j])
		j += 1	
	while(i < n1):
		if len(unionList) == 0 or unionList[-1] != arr1[i]:
			unionList.append(arr1[i])
		i += 1
	return unionList

if __name__ == "__main__":
	arr1 = [1, 1, 2, 3, 4, 5]
	arr2 = [2, 3, 4, 4, 5, 6]
	print(union(arr1, arr2))