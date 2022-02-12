def next_gap(gap):
    gap = (gap*10)//13
    if gap < 1:
        return 1
    return gap

def comb_sort(arr):
    n = len(arr)

    gap = n
    swapped = True
    
    while gap != 1 or swapped:
        gap = next_gap(gap)

        swapped = False
        for i in range(0,n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i+gap], arr[i]
                swapped = True

arr = [ 8, 4, 1, 3, -44, 23, -6, 28, 0]
comb_sort(arr)
print(arr)
