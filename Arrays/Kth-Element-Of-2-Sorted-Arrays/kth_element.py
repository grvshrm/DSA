def find(A, B, k_req): 
# Complexity : Time - O(k), Space - O(1)
	i, j, k = 0, 0, 0
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			k += 1
			if k == k_req:
				return A[i]
			i += 1
		else:
			k += 1
			if k == k_req:
				return B[j]	 
			j += 1
	while i < len(A):
		k += 1
		if k == k_req:
				return A[i]
		i += 1
	while j < len(B):
		k += 1
		if k == k_req:
				return B[j]
		j += 1

if __name__ == "__main__":
    A = [2, 3, 6, 7, 9]
    B = [1, 4, 8, 10]
    k = 5
    print(find(A, B, k))