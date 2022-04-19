def count_inversion(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                count += 1

    return count

def mergesort(arr):
    inv_count = 0
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        inv_count += mergesort(left)
        inv_count += mergesort(right)
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                inv_count += len(left) - i 
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return inv_count

from heapq import heappush, heappop
from bisect import bisect, insort
def count_inversion(arr):
    N = len(arr)
    if N <= 1:
        return 0
    
    sort_list = []
    result = 0

    for i,v in enumerate(arr):
        heappush(sort_list, (v, i))

    x = []
    while sort_list:
        v, i = heappop(sort_list)
        y = bisect(x, i)
        print(x, i, y, i - y)

        result += i - y
        insort(x, i)
    return result


arr = [1, 5, 3]
print(count_inversion(arr))
