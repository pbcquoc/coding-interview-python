def consecutive_number(arr, n):
    arr.sort()

    count = 1
    for i in range(n-1):
        if arr[i] +1 != arr[i+1]:
            count += 1

    return count

arr = [ 100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59 ]
print(consecutive_number(arr, len(arr)))

