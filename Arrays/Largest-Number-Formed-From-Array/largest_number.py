import functools
def myCompare(x, y):
    xy = x
    yx = y
    countx = 0
    county = 0
    while (x > 0):
        countx += 1
        x //= 10
    while (y > 0):
        county += 1
        y //= 10
    x = xy
    y = yx
    while (countx):
        countx -= 1
        yx *= 10
    while (county):
        county -= 1
        xy *= 10
    yx += x
    xy += y
    return 1 if xy > yx else -1

def largestNumber(arr):
# Complexity : Time - O(n*log(n)), Space - O(1)
    arr.sort(key=functools.cmp_to_key(myCompare))
    arr.reverse()
    return "".join(map(str, arr))

"""def largestNumber(array):
# Complexity : Time - O(n^2), Space - O(x), x = no. of digits in result
	if len(array)==1: 
		return str(array[0])
	for i in range(len(array)):
		array[i]=str(array[i])
	for i in range(len(array)):
		for j in range(1+i,len(array)):
			if array[j]+array[i]>array[i]+array[j]:
				array[i],array[j]=array[j],array[i]
	result=''.join(array)
	if(result=='0'*len(result)):
		return '0'
	else:
		return result"""

if __name__ == "__main__":
	a = [54, 546, 548, 60]
	print(largestNumber(a))
