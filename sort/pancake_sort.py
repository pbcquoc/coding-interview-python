def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i

    return mi

def pancake_sort(arr, n):
    curr_size = n
    while curr_size > 1:
        mi = find_max(arr, curr_size)
        if mi != curr_size -1:
            flip(arr, mi)
            flip(arr, curr_size -1)

        curr_size -= 1

arr = [23, 10, 20, 11, 12, 6, 7]
pancake_sort(arr, len(arr))
print(arr)
