def find_pivot(arr, l, r):
    while (l < r - 1):
        m = (l+r)//2
        if arr[m] > arr[r]:
            l = m
        if arr[m] < arr[l]:
            r = m
    return l

def binary_search(arr, l, r, key):
    while(l <= r):
        m = (l+r)//2
        if arr[m] == key:
            return m
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key:
            r = m - 1

    return -1

arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
n = len(arr1) 
key = 0

pivot = find_pivot(arr1, 0, n-1)
left = binary_search(arr1, 0, pivot, key)
right = binary_search(arr1, pivot+1, n-1, key)
print(left, right)
