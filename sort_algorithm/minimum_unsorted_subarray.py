def unsorted_subarray(arr, n):
    i = 0
    j = n - 1

    while arr[i + 1] >= arr[i]:
        i += 1

    while arr[j-1] <= arr[j]:
        j -= 1
    
    
    min_value = min(arr[i+1:j-1])
    max_value = max(arr[i+1:j-1])
    
    i = 0
    j = n - 1
    while min_value >= arr[i]:
        i += 1

    while max_value <= arr[j]:
        j -= 1

    print(i, j)

arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
unsorted_subarray(arr, len(arr))
