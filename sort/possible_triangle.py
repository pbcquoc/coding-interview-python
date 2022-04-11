def possible_triangle(arr, n):
    arr.sort()

    for i in range(n-2):
        if arr[i] + arr[i+1] > arr[i+1]:
            return True

    return False

arr = [5, 4, 3, 1, 2]
print(possible_triangle(arr, len(arr)))
