"""
https://www.geeksforgeeks.org/minimum-swaps-reach-permuted-array-2-positions-left-swaps-allowed/
"""

def merge(arr, tmp, left, mid, right):
    inv_count = 0

    i = left
    j = mid
    k = left
    
    while i <= mid -1 and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
            inv_count += (mid - i)

        k += 1
    
    while i <= mid - 1:
        tmp[i] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[j] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right+1):
        arr[i] = tmp[i]

    return inv_count

def _merge_sort(arr, tmp, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right)//2
        
        inv_count += _merge_sort(arr, tmp, left, mid)
        inv_count += _merge_sort(arr, tmp, mid+1, right)

        inv_count += merge(arr, tmp, left, mid+1, right) 
        
    return inv_count

def merge_sort(arr, n):
    tmp = [0]*n
    return _merge_sort(arr, tmp, 0, n-1)

def min_swaps(arr, n):
    for i in range(n):
        if (arr[i] -1) - i > 2:
            return -1

    num_inversion = merge_sort(arr, n)

    return num_inversion

arr = [1, 2, 5, 3, 4]
print(min_swaps(arr, len(arr)))
