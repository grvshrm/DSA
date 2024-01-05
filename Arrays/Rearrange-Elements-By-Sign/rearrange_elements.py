def rearrange(arr, n):
# Complexity : Time - O(n), Space - O(n). Works for equal/unequal no. of negatives and positives
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]
        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1
    return arr

"""def rearrange(arr, n):
# Complexity : Time - O(n), Space - O(n). Not for unequal no. of negatives and positives
    pos, neg = 0, 1
    ans = [0]*n
    for i in range(n):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    return ans"""

"""def rearrange(arr, n):
# Complexity : Time - O(n), Space - O(n). Not for unequal no. of negatives and positives
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for i in range(n//2):
        arr[i * 2] = pos[i]
        arr[i * 2 + 1] = neg[i]
    return arr"""

if __name__ == "__main__":
    arr = [3, 1, -2, -5, 2, -4, 6, 4]
    n = len(arr) 
    print("Original Array") 
    print(arr) 
    print("Modified Array") 
    print(rearrange(arr, n)) 