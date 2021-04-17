"""

"""

def bubble_sort(arr, n):
    if n == 1: return
    
    for j in range(0, n - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    bubble_sort(arr, n -1)



arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr, len(arr))
print(arr)
