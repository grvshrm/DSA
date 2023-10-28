def getSum(X):
	sum=0
	for i in X:
		sum+=i
	return sum

def getTarget(A,B):
    sum1=getSum(A)
    sum2=getSum(B)
    if( (sum1-sum2)%2!=0):
        return 0
    return (sum1-sum2)//2

def findSwapValues(A,B):
# Complexity : Time - O(m + n), Space - O(s + t), s and t represent the number of distinct elements in the arrays
    x, y = {}, {}
    s1, s2 = 0, 0
    m, n = len(A), len(B)
    for i in range(m):
        s1 += A[i]
        x[A[i]] = x.get(A[i], 0) + 1
    for i in range(n):
        s2 += B[i]
        y[B[i]] = y.get(B[i], 0) + 1
    if (s1 - s2) % 2:
        print("No such values exist.")
        return
    for p in x:
        q = ((s2 - s1)//2) + p
        if q in y:
            print(p, q)
            return
    print("No such values exist.")

"""def findSwapValues(A,B):
# Complexity : Time - O(nlog(n) + mlog(m)), Space - O(1)
    A.sort()
    B.sort()
    target=getTarget(A,B)
    if(target==0):
        return
    i,j=0,0
    while(i<len(A) and j<len(B)):
        diff=A[i]-B[j]
        if diff == target:
            print (A[i],B[j])
            return
        elif diff <target:
            i+=1
        else:
            j+=1"""

"""def findSwapValues(A,B):
# Complexity : Time - O(n*m), Space - O(1)
    target=getTarget(A,B)
    if target==0:
        return
    flag=False
    val1,val2=0,0
    for i in A:
        for j in B:
            if i-j == target:
                val1=i
                val2=j
                flag=True
                break
        if flag==True:
            break
    print (val1,val2)
    return"""

"""def findSwapValues(A,B):
# Complexity : Time - O(n*m), Space - O(1)
	sum1=getSum(A)
	sum2=getSum(B)
	k=False
	val1,val2=0,0
	for i in A:
		for j in B:
			newsum1=sum1-i+j
			newsum2=sum2-j+i	
			if newsum1 ==newsum2:
				val1=i
				val2=j
				k=True
				break
		if k==True:
			break
	print (val1,val2)
	return"""

if __name__ == "__main__": 
    A=[1,2,3,4,5]
    B=[6,8,3]
    findSwapValues(A,B)