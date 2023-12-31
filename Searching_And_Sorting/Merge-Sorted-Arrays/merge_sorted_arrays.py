import bisect
def mergeArrays(a, b, n, m):
# Complexity : Time - O(nlog(n) + mlog(m)), Space - O(N)
	mp=[]
	for i in range(n):
		bisect.insort(mp, a[i])
	for i in range(m):
		bisect.insort(mp, b[i])
	for i in mp:
		print(i,end=' ')

"""def mergeArrays(arr1, arr2, n1, n2):
# Complexity : Time - O(n1 + n2), Space - O(n1 + n2)
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else:
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	while i < n1:
		arr3[k] = arr1[i];
		k = k + 1
		i = i + 1
	while j < n2:
		arr3[k] = arr2[j];
		k = k + 1
		j = j + 1
	print("Array after merging")
	for i in range(n1 + n2):
		print(str(arr3[i]), end = " ")"""

if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    n1 = len(arr1)
    arr2 = [2, 4, 6, 8]
    n2 = len(arr2)
    mergeArrays(arr1, arr2, n1, n2)