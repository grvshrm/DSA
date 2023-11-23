def search(arr, l, h, key):
# Complexity : Time - O(log n), Space - O(1)
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    if arr[l] <= arr[mid]:
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        else:
            return search(arr, mid + 1, h, key)
    else:
        if key >= arr[mid] and key <= arr[h]:
            return search(arr, mid + 1, h, key)
        else:
            return search(arr, l, mid-1, key)

"""def search(arr, 0, n, key):
# Complexity : Time - O(n), Space - O(1)
	for i in range(n+1):
		if arr[i] == key:
			return i
	return -1"""

if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    index = search(arr, 0, len(arr)-1, key)
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")