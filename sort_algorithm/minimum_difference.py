def minimum_difference(arr, n, m):
    arr.sort()
    
    min_diff = arr[n-1] - arr[0]
    for i in range(n - m + 1):
        diff = arr[i+m-1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
n = len(arr)
print(minimum_difference(arr, n, m))
