def subArraySum(arr, n, Sum):
# Complexity : Time - O(n), Space - O(n) : Handles Negatives
    Map = {}
    curr_sum = 0
    for i in range(0, n):
        curr_sum = curr_sum + arr[i]
        if curr_sum == Sum:
            print("Sum found between indexes 0 to", i)
            return
        if (curr_sum - Sum) in Map:
            print("Sum found between indexes",
                  Map[curr_sum - Sum] + 1, "to", i)
            return
        Map[curr_sum] = i
    print("No subarray with given sum exists")

"""def subArraySum(arr, n, sum_):
# Complexity : Time - O(n), Space - O(1) : Doesn't handle Negatives
    currentSum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while currentSum > sum_ and start < i-1:
            currentSum = currentSum - arr[start]
            start += 1
        if currentSum == sum_:
            print("Sum found between indexes %d and %d" % (start, i-1))
            return 1
        if i < n:
            currentSum = currentSum + arr[i]
        i += 1
    print("No subarray found")
    return 0"""

"""def subArraySum(arr, n, sum):
# Complexity : Time - O(n^2), Space - O(1) : Handles Negatives
	for i in range(0,n):
		currentSum = arr[i]
		if(currentSum == sum):
			print("Sum found at index",i)
			return
		else:
			for j in range(i+1,n):
				currentSum += arr[j]
				if(currentSum == sum):
					print("Sum found between indexes",i,"and",j)
					return
	print("No Subarray Found")"""

if __name__ == "__main__":
	arr = [15,2,4,8,9,5,10,23]
	n = len(arr)
	sum = 23
	subArraySum(arr, n, sum)