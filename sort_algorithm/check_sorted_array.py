def array_sorted(arr):
    if len(arr) == 1 or len(arr) == 0:
        return True
    
    return arr[0] <= arr[1] and array_sorted(arr[1:])

arr = [20, 19, 23, 45, 78, 88]
print(array_sorted(arr))


