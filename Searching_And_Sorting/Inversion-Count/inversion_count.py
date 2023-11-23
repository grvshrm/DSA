from heapq import heappush, heappop
from bisect import bisect, insort

def getInvCount(A, N):
# Complexity : Time - O(n*(log n)), Space - O(n)
    if N <= 1:
        return 0
    sortList = []
    result = 0
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
    x = []
    while sortList:
        v, i = heappop(sortList)
        y = bisect(x, i)
        result += i - y
        insort(x, i)
    return result

"""def getInvCount(arr, n):
# Complexity : Time - O(n^2), Space - O(1)
	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1
	return inv_count"""

if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    print("Number of inversions are", getInvCount(arr, n))