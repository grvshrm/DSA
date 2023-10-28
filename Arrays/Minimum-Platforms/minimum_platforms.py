def findPlatform(arrival, departure, n):
# Complexity : Time - O(n), Space - O(1)
    platform = [0] * 2360
    requiredPlatform = 1
    for i in range(n):
        platform[arrival[i]] += 1
        platform[departure[i]] -= 1
    for i in range(1, 2360):
        platform[i] = platform[i] + platform[i - 1]
        requiredPlatform = max(requiredPlatform, platform[i])
    return requiredPlatform

"""def findPlatform(arr, dep, n):
# Complexity : Time - O(n*log(n))), Space - O(1)
    arr.sort()
    dep.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1
        elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1
        if (plat_needed > result):
            result = plat_needed
    return result"""

"""def findPlatform(arr, dep, n):
# Complexity : Time - O(n^2), Space - O(1)
	plat_needed = 1
	result = 1
	for i in range(n):
		plat_needed = 1
		for j in range(n):
			if i != j:
				if (arr[i] >= arr[j] and dep[j] >= arr[i]):
					plat_needed += 1
		result = max(result, plat_needed)
	return result"""

if __name__ == '__main__':
	arr = [100, 300, 500]
	dep = [900, 400, 600]
	n = len(arr)
	print("{}".format(findPlatform(arr, dep, n)))