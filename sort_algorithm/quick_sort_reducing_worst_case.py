def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p -1)
        quick_sort(arr, p+1, high)

def quick_sort(arr, low, high):
    while low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        low = p + 1

def quick_sort(arr, low, high):
    while low < high:
        p = partition(arr, low, high)

        if p - low < high - p:
            quick_sort(arr, low, p - 1)
            low = p + 1
        else:
            quick_sort(arr, p + 1, high)
            high = p - 1

a = [1,4,2,7,5]
quick_sort(a, 0, len(a) - 1)
print(a)

