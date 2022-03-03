"""insertion sort is effience for k nearly sorted array
"""

def insertion_sort(arr, n):
    for i in range(1, n):
        j = i
        key = arr[i]
        
        while arr[j -1] > key and j > 0:
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = key

from heapq import heappop, heappush, heapify

def sort_k(arr, n, k):
    heap = arr[:k]
    heapify(heap)

    target_index = 0
    for i in range(k, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[i])
        target_index += 1

    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1

k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)

sort_k(arr, len(arr), k)
print(arr)
