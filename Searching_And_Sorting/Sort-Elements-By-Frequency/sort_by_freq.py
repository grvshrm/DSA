from collections import defaultdict
from queue import PriorityQueue

"""class Compare:
    def __init__(self, freq, val, ind):
        self.freq = freq
        self.val = val
        self.ind = ind
 
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.ind < other.ind
        return self.freq > other.freq
 
def sortByFrequency(arr, n):
    mpp = defaultdict(int)
    ind_map = defaultdict(int)
    for a in arr:
        mpp[a] += 1
    for ind, val in enumerate(arr):
        ind_map[val] = ind if ind_map.get(val) == 0 else ind_map.get(val)
    for a in arr:
        ind_map[a] = arr.index(a)
    max_heap = PriorityQueue()
    for element, freq in mpp.items():
        max_heap.put(Compare(freq, element, ind_map[element]))
    i = 0
    while not max_heap.empty():
        item = max_heap.get()
        freq = item.freq
        val = item.val
        for _ in range(freq):
            arr[i] = val
            i += 1
    return arr"""

class ele:
	def __init__(self):
		self.count = 0
		self.index = 0
		self.val = 0

def mycomp(a):
	return a.val

def mycomp2(a):
	return (a.count, -a.index)

def sortByFrequency(arr, n):
# Complexity : Time - O(n*log(n)), Space - O(N)
	element = [None for _ in range(n)]
	for i in range(n):
		element[i] = ele()
		element[i].index = i
		element[i].count = 0
		element[i].val = arr[i]
	element.sort(key=mycomp)
	element[0].count = 1
	for i in range(1, n):
		if (element[i].val == element[i - 1].val):
			element[i].count += element[i - 1].count + 1
			element[i - 1].count = -1
			element[i].index = element[i - 1].index
		else:
			element[i].count = 1
	element.sort(key=mycomp2)
	index = 0
	for i in range(n - 1, -1, -1):
		if (element[i].count != -1):
			for j in range(element[i].count):
				arr[index] = element[i].val
				index += 1

if __name__ == '__main__':
    arr = [2, 6, 2, 6, 5, 9999999, -1, 5, 8, 8, 8]
    n = len(arr)
    sortByFrequency(arr, n)
    print(*arr)