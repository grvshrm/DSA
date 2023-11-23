def getMedian( A, B, n, m):
# Complexity : Time - O(min(log(n), log(m))), Space - O(1)
    if (n > m):
        return getMedian(B, A, m, n)
    start = 0
    end = n
    realmidinmergedarray = (n + m + 1) // 2

    while (start <= end):
        mid = (start + end) // 2
        leftAsize = mid
        leftBsize = realmidinmergedarray - mid
        leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
        leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
        rightA = A[leftAsize] if (leftAsize < n) else float('inf')
        rightB = B[leftBsize] if (leftBsize < m) else float('inf')
        if leftA <= rightB and leftB <= rightA:
            if ((m + n) % 2 == 0):
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            return max(leftA, leftB)
        elif (leftA > rightB):
            end = mid - 1
        else:
            start = mid + 1
            
"""def getMedian(a, b, n1, n2):
# Complexity : Time - O(n+m), Space - O(1)
    i = 0
    j = 0
    m1, m2 = -1, -1
    n = (n1 + n2)
    ind2 = n//2
    ind1 = ind2 - 1
    count = 0
    while(i < n1 and j < n2):
        if(a[i] < b[j]):
            if(count == ind1):
                m1 = a[i]
            if(count == ind2):
                m2 = a[i]
            count += 1
            i +=1
        else:
            if(count == ind1):
                m1 = b[j]
            if(count == ind2):
                m2 = b[j]
            count += 1
            j +=1
    while(i < n1):
        if(count == ind1):
            m1 = a[i]
        if(count == ind2):
            m2 = a[i]
        count += 1
        i +=1
    while(j < n2):
        if(count == ind1):
            m1 = b[j]
        if(count == ind2):
            m2 = b[j]
        count += 1
        j +=1

    if n%2 != 0:
        return m2
    else:
        return (m1+m2)/2"""

if __name__ == '__main__':
    ar1 = [1, 900]
    ar2 = [5, 8, 10, 20]
    n1 = len(ar1)
    n2 = len(ar2)
    print(getMedian(ar1, ar2, n1, n2))