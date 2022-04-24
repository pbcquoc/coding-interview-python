def maximum_height(arr, n):
    result = 1
    for i in range(1, n):
        y = i*(i+1)/2
        if y < n:
            result = i
        else:
            break

    return result

arr = [40, 100, 20, 30]
print(maximum_height(arr, len(arr)))
