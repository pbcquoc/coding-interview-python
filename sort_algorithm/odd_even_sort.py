def old_even_sort(arr, n):
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        for i in range(1, n -1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0

arr = [34, 2, 10, -9]
old_even_sort(arr, len(arr))
print(arr)

