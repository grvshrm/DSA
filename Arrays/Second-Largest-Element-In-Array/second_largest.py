def secondLargestElement(arr):
# Complexity : Time - O(n), Space - O(1)
    lar = arr[0]
    sec_lar = -1
    for i in range(1, len(arr)):
        if(arr[i] > lar):
            sec_lar = lar
            lar = arr[i]
        elif(arr[i] < lar and arr[i] > sec_lar):
             sec_lar = arr[i]
    return sec_lar

"""def secondLargestElement(arr):
# Complexity : Time - O(2n), Space - O(1)
    lar = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > lar):
            lar = arr[i]
    sec_lar = -1
    for i in range(0, len(arr)):
        if(arr[i] > sec_lar and arr[i] != lar):
            sec_lar = arr[i]
    return sec_lar"""

"""def secondLargestElement(arr):
# Complexity : Time - O(n*(log(n)) + n), Space - O(1)
	arr.sort()
	lar = arr[-1]
	sec_lar = -1
	i = len(arr) - 2
	while(i >= 0):
		if(arr[i] != lar):
			sec_lar = arr[i]
			break
	return sec_lar"""

if __name__ == "__main__":
	arr = [3, 2, 1, 6, 5, 2]
	print(secondLargestElement(arr))