def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index += 1
        elif arr[index] >= arr[index -1]:
            index += 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -=1

    return arr

arr = [ 34, 2, 10, -9]
print(gnome_sort(arr, len(arr)))

