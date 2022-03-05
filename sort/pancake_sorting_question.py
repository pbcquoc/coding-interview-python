"""https://www.geeksforgeeks.org/a-pancake-sorting-question/
"""

def ceil_search(arr, low, high, x):
    print(low, high)
    if x <= arr[low]:
        return low
    if x > arr[high]:
        return -1
    
    if high - low == 1 and arr[low] <= x <= arr[high]:
        return high

    mid = (high + low)//2

    if arr[mid] == x:
        return mid

    if arr[mid] > x:
        return ceil_search(arr, low, mid, x)

    if arr[mid] < x:
        return ceil_search(arr, mid, high, x)

def flip(arr, i):
    start = 0
    while i > start:
        arr[i], arr[start] = arr[start], arr[i]
        start += 1
        i -= 1

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        j = ceil_search(arr, 0, i-1, arr[i])

        if j != -1:
            flip(arr, j-1)
            flip(arr, i-1)
            flip(arr, i)
            flip(arr, j)


arr=[18, 40, 35, 12, 30, 35, 20, 6, 90, 80]

insertion_sort(arr)
print(arr)
