def noble_integer(arr, n):
    arr.sort()

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            continue

        if arr[i] == n - i - 1:
            return arr[i]
    
    if arr[n-1] == 0:
        return 0
    
    return -1

arr = [10, 3, 20, 40, 2]
print(noble_integer(arr, len(arr)))
