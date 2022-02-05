def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)

arr = [10, 7, 8, 9, 1, 5] 
quick_sort(arr, 0, len(arr)-1)
print(arr)
