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
    

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [arr[l+i] for i in range(n1)]
    R = [arr[m+ 1 + i] for i in range(n2)]

    i = 0
    j = 0
    k = l

    while i < n1 and L[i] < 0:
        arr[k] = L[i]
        k += 1
        i += 1

    while j < n2 and R[j] < 0:
        arr[k] = R[j]
        k += 1
        j += 1

    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1

def reverse(arr, l, r):
    if l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        reverse(arr, l, r)

def merge_inplace(arr, l, m, r):
    i = l
    j = m + 1

    while i <= m and arr[i] < 0:
        i += 1

    while j <= r and arr[j] < 0:
        j += 1

    reverse(arr, i, m)
    reverse(arr, m + 1, j - 1)
    reverse(arr, i, j - 1)


def move_negative_merge_sort(arr, l, r):
    if l < r:
        mid = (l+r)//2

        move_negative_merge_sort(arr, l, mid)
        move_negative_merge_sort(arr, mid+1, r)
        #merge(arr, l, mid, r)
        merge_inplace(arr, l, mid, r)

arr = [5, 5, -3, 4, -8, 0, -7, 3, -9, -3, 9, -2, 1]
move_negative_merge_sort(arr, 0, len(arr)-1)
print(arr)
