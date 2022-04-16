def even_odd_sort(arr, n):
    l, r = 0, n - 1
    
    i = 0
    while l < r:
        
        if arr[i] % 2 != 0:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
        else:
            arr[r], arr[i] = arr[i], arr[r]
            r -= 1
        i += 1
        
    odd = arr[:l]
    even = arr[l:]
    odd.sort(reverse=True)
    even.sort()

    odd.extend(even)

    return odd

arr = [1, 3, 2, 7, 5, 4, 6]
print(even_odd_sort(arr, len(arr)))
print(arr)
