def shell_sort(arr):
    gap = len(arr)//2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1
            
            print(i, j, gap)

            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k-gap], arr[k] = arr[k], arr[k-gap]

                k -= 1
        gap //= 2

arr2 = [12, 34, 54, 2, 3]
shell_sort(arr2)
print(arr2)

