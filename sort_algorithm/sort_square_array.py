def sort_square(arr, n):
    
    for k in range(n):
        if arr[k] >= 0:
            break
    
    i = k - 1
    j = k
    ind = 0

    tmp = [0]*n
    while i >= 0 and j < n:
        if arr[i]*arr[i] < arr[j]*arr[j]:
            tmp[ind] = arr[i]*arr[i]
            i -= 1
        else:
            tmp[ind] = arr[j]*arr[j]
            j += 1

        ind += 1

    while i >= 0:
        tmp[ind] = arr[i]*arr[i]
        ind += 1
        i -= 1
    
    while j < n:
        tmp[ind] = arr[j]*arr[j]
        ind += 1
        j += 1

    for i in range(n):
        arr[i] = tmp[i]

def sort_square(arr, n):
    left = 0
    right = n - 1
    index = n - 1
    result = [0]*n

    while index >= 0:
        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left]*arr[left]
            left += 1
        else:
            result[index] = arr[right]*arr[right]
            right -= 1
        index -= 1

    for i in range(n):
        arr[i] = result[i]

    return arr

arr = [-6, -3, -1, 2, 4, 5 ]
sort_square(arr, len(arr))
print(arr)
