"""
https://www.geeksforgeeks.org/minimum-swaps-reach-permuted-array-2-positions-left-swaps-allowed/
"""

def merge(arr, tmp, left, mid, right):
    pass

def _merge_sort(arr, tmp, left, right):
    if left < right:
        mid = (left + right)//2
        
        inv_count  = _merge_sort(arr, tmp, left, mid)
        inv_count += _merge_sort(arr, tmp, mid+1, right)

        inv_count += merge(arr, tmp, left, mid+1, right) 
        
        return inv_count

def min_swaps(arr, n):
    for i in range(n):
        if arr[i] - i > 2:
            return -1

    num_inversion = merge_sort(arr, n)

    return num_inversion

arr = [1, 2, 5, 3, 4]
print(num_swaps(arr, len(arr)))
