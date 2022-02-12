def pigeonhole_sort(arr):
    my_min = min(arr)
    my_max = max(arr)

    size = my_max - my_min + 1
    holes = [0]*size

    for x in a:
        holes[x - my_min] += 1
    

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + my_min
            i += 1

a = [8, 3, 2, 7, 4, 6, 8]
pigeonhole_sort(a)
print(a)
