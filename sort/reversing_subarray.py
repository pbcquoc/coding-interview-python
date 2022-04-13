def check_reverse(arr, n):
    tmp = sorted(arr)

    for front in range(n):
        if arr[front] != tmp[front]:
            break

    for back in range(n-1, -1, -1):
        if arr[back] != tmp[back]:
            break
    
    if front >= back:
        return True

    while front != back:
        front += 1
        if arr[front - 1] < arr[front]:
            return False

    return True

arr = [1, 2, 5, 4, 3]
print(check_reverse(arr, len(arr)))
