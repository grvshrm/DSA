def sort012(a, arr_size):
# Complexity : Time - O(n), Space - O(1)
	lo = 0
	hi = arr_size - 1
	mid = 0
	while mid <= hi:
		# If the element is 0
		if a[mid] == 0:
			a[lo], a[mid] = a[mid], a[lo]
			lo = lo + 1
			mid = mid + 1
		# If the element is 1
		elif a[mid] == 1:
			mid = mid + 1
		# If the element is 2
		else:
			a[mid], a[hi] = a[hi], a[mid]
			hi = hi - 1
	return a

def printArray(a):
	for k in a:
		print(k, end=' ')

if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    arr_size = len(arr)
    arr = sort012(arr, arr_size)
    printArray(arr)