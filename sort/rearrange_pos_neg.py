def rotate(arr, l, r):
    tmp = arr[r]
    for j in range(r, l-1, -1):
        arr[j] = arr[j-1]
    arr[l] = tmp

def move_negative_qsort(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
            if j - i >= 2:
                rotate(arr, i+1, j)

def move_negative_insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        if key >= 0:
             continue 

        j = i - 1
        while j >= 0 and arr[j] >= 0:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    

            



arr = [5, 5, -3, 4, -8, 0, -7, 3, -9, -3, 9, -2, 1]
move_negative_insertion_sort(arr, len(arr))
print(arr)
