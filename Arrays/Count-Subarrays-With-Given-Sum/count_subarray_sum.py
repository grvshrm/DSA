from collections import defaultdict

def findSubarrayCount(arr, n, k):
# Complexity : Time - O(n), Space - O(n)
    mpp = defaultdict(int)
    preSum, cnt = 0, 0
    mpp[0] = 1
    for i in range(n):
        preSum += arr[i]
        remaining = preSum - k
        cnt += mpp[remaining]
        mpp[preSum] += 1
    return cnt

"""def findSubarrayCount(arr, n, k):
# Complexity : Time - O(n^2), Space - O(1)
    cnt = 0
    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum += arr[j]
            if subarray_sum == k:
                cnt += 1
    return cnt"""

"""def findSubarrayCount(arr, n, k):
# Complexity : Time - O(n^3), Space - O(1)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            subarray_sum = sum(arr[i:j+1])
            if subarray_sum == k:
                cnt += 1
    return cnt"""

if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    n = len(arr)
    k = 6
    print(findSubarrayCount(arr, n, k))