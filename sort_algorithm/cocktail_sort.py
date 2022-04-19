def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n -1
    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if swapped == False:
            break

        swapped = False
        
        for i in range(end - 1, start -1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        start = start + 1

a = [5, 1, 4, 2, 8, 0, 2]
cocktail_sort(a)
print(a)
