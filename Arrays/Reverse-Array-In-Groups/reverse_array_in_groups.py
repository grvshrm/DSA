def reverse(arr, n, k):
# Complexity : Time - O(n), Space - O(1)
	i = 0
	while(i<n):
		left = i 
		right = min(i + k - 1, n - 1) 
		# Reverse the sub-array [left, right]
		while (left < right):
			arr[left], arr[right] = arr[right], arr[left]
			left+= 1
			right-=1
		i+= k
	
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8] 

    k = 3
    n = len(arr) 
    reverse(arr, n, k)

    for i in range(0, n):
            print(arr[i], end =" ")