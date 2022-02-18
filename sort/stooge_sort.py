def stooge_sort(arr, l, h):
    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    if h - l > 1:
        t = (h -l + 1)//3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)

arr = [2, 4, 5, 3, 1]
stooge_sort(arr, 0, len(arr) - 1)
print(arr)
