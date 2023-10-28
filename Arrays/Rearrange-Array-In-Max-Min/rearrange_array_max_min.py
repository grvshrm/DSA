def rearrange(arr, n):
# Complexity : Time - O(n), Space - O(1)
    max_idx = n - 1
    min_idx = 0
    max_elem = arr[n-1] + 1
    for i in range(0, n) :
        if i % 2 == 0 :
            arr[i] += (arr[max_idx] % max_elem ) * max_elem
            max_idx -= 1
        else :
            arr[i] += (arr[min_idx] % max_elem ) * max_elem
            min_idx += 1
    for i in range(0, n) :
        arr[i] = arr[i] / max_elem 
"""
def rearrange(arr, n): 
# Complexity : Time - O(n), Space - O(n)
	temp = n*[None] 
	small, large = 0, n-1
	flag = True #largest element first
	for i in range(n): 
		# larger element
		if flag is True: 
			temp[i] = arr[large] 
			large -= 1
		# smaller element
		else: 
			temp[i] = arr[small] 
			small += 1
		flag = bool(1-flag) 
	for i in range(n): 
		arr[i] = temp[i] 
	return arr 
"""

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6] 
    n = len(arr) 
    print("Original Array") 
    print(arr) 
    print("Modified Array") 
    print(rearrange(arr, n)) 