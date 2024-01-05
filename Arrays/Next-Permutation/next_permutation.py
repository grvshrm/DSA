def reverse(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

def nextPermutation(arr):
# Complexity : Time - O(n), Space - O(1)
	ind = -1
	n = len(arr)
	for i in range(n-2, -1 , -1):
		if arr[i] < arr[i+1]:
			ind = i
			break
	if ind == -1:
		return arr.reverse()
	for i in range(n-1, ind, -1):
		if arr[i] > arr[ind]:
			arr[i], arr[ind] = arr[ind], arr[i]
			break
	reverse(arr, ind+1, n-1) 
	return arr

if __name__ == '__main__': 
	num_arr = [1, 3, 2]
	print(nextPermutation(num_arr))