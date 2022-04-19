def max_triplet_product(arr, n):
    max_a, max_b, max_c = -1000, -1000, -1000
    min_a, min_b = 1000, 1000

    for i in range(n):
        if arr[i] > max_a:
            max_c = max_b
            max_b = max_a
            max_a = arr[i]
        elif arr[i] > max_b:
            max_c = max_b
            max_b = arr[i]
        elif arr[i] > max_c:
            max_c = arr[i]

        if arr[i] < min_a:
            min_b = min_a
            min_a = arr[i]
        elif arr[i] < min_b:
            min_b = arr[i]

    return max(max_a*max_b*max_c, min_a*min_b*max_a)
        

arr = [ 1, -4, 3, -6, 7, 0 ]
print(max_triplet_product(arr, len(arr)))
