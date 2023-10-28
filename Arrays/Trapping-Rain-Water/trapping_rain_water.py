def maxWater(arr, n):
# Complexity : Time - O(n), Space - O(1)
    left = 0
    right = n - 1
    rightMax = 0
    leftMax = 0
    water = 0
    while(left <= right):
        if(arr[left] <= arr[right]):
            if(arr[left] > leftMax):
                leftMax = arr[left]
            else:
                water += (leftMax - arr[left])
            left += 1
        else:
            if(arr[right] > rightMax):
                rightMax = arr[right]
            else:
                water += (rightMax - arr[right])
            right -= 1
    return water

"""def maxWater(arr, n):  
# Complexity : Time - O(n), Space - O(n)
    left = [0]*n  
    right = [0]*n 
    water = 0
    left[0] = arr[0] 
    for i in range(1, n): 
        left[i] = max(left[i-1], arr[i]) 
    right[n-1] = arr[n-1] 
    for i in range(n-2, -1, -1): 
        right[i] = max(right[i + 1], arr[i]) 
    for i in range(0, n): 
        water += min(left[i], right[i]) - arr[i] 
    return water"""

"""def maxWater(arr, n): 
# Complexity : Time - O(n^2), Space - O(1)
	res = 0
	for i in range(1, n - 1): 
		left = arr[i] 
		for j in range(i): 
			left = max(left, arr[j]) 
		right = arr[i] 
		for j in range(i + 1, n): 
			right = max(right, arr[j]) 
		res = res + (min(left, right) - arr[i]) 
	return res"""

if __name__ == "__main__": 
	arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
	# arr = [3, 0, 2, 0, 4]
	n = len(arr) 
	print(maxWater(arr, n)) 