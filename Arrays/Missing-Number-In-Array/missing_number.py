def findMissing(arr, N):
# Complexity : Time - O(n), Space - O(1)
	arr_xor = 0
	num_xor = 0
	for num in arr:
		arr_xor ^= num
	for num in range(1, N+2):
		num_xor ^= num
	print(arr_xor ^ num_xor)
	
"""def findMissing(arr, N):
    n_sum = ((N + 1) * (N + 2)) // 2
    arr_sum = sum(arr)
    print(n_sum - arr_sum)"""

"""def findMissing(arr, N):
    arr_sum = sum(arr)
    n_sum = 0
    for num in range(1, N+2):
        n_sum += num
    print(n_sum - arr_sum)"""

if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)
	findMissing(arr, N)