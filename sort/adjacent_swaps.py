"""
https://www.geeksforgeeks.org/number-swaps-sort-adjacent-swapping-allowed/
"""
def merge(arr, tmp, left, mid, right):
    
    i = left
    j = mid
    k = left
    
    inv_count = 0
    while i <= mid -1 and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k+=1
            i+=1
        else:
            tmp[k] = arr[j]
            k+=1
            j+=1
            
            inv_count += (mid - i)


