"""
https://www.geeksforgeeks.org/sort-array-applying-given-equation/
"""

def sort_array(arr, n, A, B, C):
    for i in range(n):
        arr[i] = A*arr[i]*arr[i] + B*arr[i] + C

    index = 0
    maxe = arr[0]

    for i in range(n):
        if maxe < arr[i]:
            maxe = arr[i]
            index = i
    
    i = 0
    j = n - 1
    k = 0
    tmp = [0]*n

    while i <= index and j > index:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1
            j -= 1

    while i <= index:
        tmp[k] = arr[i]
        k += 1
        i += 1

    while j > index:
        tmp[k] = arr[j]
        k += 1
        j -= 1
    
    
    for i in range(n):
        arr[i] = tmp[i]

arr = [-21, -15, 12, 13, 14]
A = -6
B = -7
C = 2
sort_array(arr, len(arr), A, B, C)
print(arr)
