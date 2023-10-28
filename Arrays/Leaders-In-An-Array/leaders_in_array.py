def printLeaders(arr, size):
# Complexity : Time - O(n), Space - O(1)
    max_from_right = arr[size-1]   
    print (max_from_right,end=' ')    
    for i in range( size-2, -1, -1):        
        if max_from_right < arr[i]:        
            print (arr[i],end=' ')
            max_from_right = arr[i]
"""
# Complexity : Time - O(n^2), Space - O(1)
def printLeaders(arr,size): 
     
    for i in range(0, size): 
        for j in range(i+1, size): 
            if arr[i]<=arr[j]: 
                break
        if j == size-1:
            print (arr[i],end=' ') 
"""

if __name__ == '__main__':
    arr = [16, 17, 4, 3, 5, 2]
    printLeaders(arr, len(arr))