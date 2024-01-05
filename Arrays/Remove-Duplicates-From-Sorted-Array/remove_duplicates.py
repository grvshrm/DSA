def removeDuplicates(arr):
# Complexity : Time - O(n), Space - O(1)
    i = 0
    for j in range(len(arr)):
        if(arr[j] != arr[i]):
            i += 1
            arr[i] = arr[j]
    print(f"Array: {arr} with Unique Elements: {i+1}")

"""def removeDuplicates(arr):
# Complexity : Time - O(n), Space - O(n)
    unique_elements = set(arr)
    i = 0
    for item in unique_elements:
        arr[i] = item
        i += 1
    print(f"Array: {arr} with Unique Elements: {len(unique_elements)}")"""

if __name__ == "__main__":
	arr = [1, 1, 2, 2, 3, 3]
	removeDuplicates(arr)