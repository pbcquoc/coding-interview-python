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

    while i <= mid - 1:
        tmp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        tmp[k] = arr[j]
        k += 1
        j += 1


    for i in range(left, right+1):
        arr[i] = tmp[i]

    return inv_count

def merge_sort(arr, tmp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        inv_count += merge_sort(arr, tmp, left, mid)
        inv_count += merge_sort(arr, tmp, mid+1, right)
        inv_count += merge(arr, tmp, left, mid+1, right)

    return inv_count

def inv_count(arr, n):
    tmp = [0]*n
    
    return merge_sort(arr, tmp, 0, n -1)

arr = [1, 20, 6, 4, 5]
print(inv_count(arr, len(arr)))

