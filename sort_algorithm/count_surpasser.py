def merge(A, aux, low, mid, high, count):
    k = i = low
    j = mid + 1
    c = 0

    while i <= mid and j <= high:
        if A[i] > A[j]:
            count[A[i]] = count.get(A[i], 0) + c
            aux[k] = A[i]
            i += 1
        else:
            aux[k] = A[j]
            j += 1
            c += 1
        k += 1

    while i <= mid:
        count[A[i]] = count.get(A[i], 0) + c
        aux[k] = A[i]
        k += 1
        i += 1

    for i in range(low, high + 1):
        A[i] = aux[i]

def mergesort(A, aux, low, high, count):
    if high <= low:
        return 

    mid = (low + high)//2

    mergesort(A, aux, low, mid, count)
    mergesort(A, aux, mid + 1, high, count)
    merge(A, aux, low, mid, high, count)

def surpasser(A):
    count ={}
    aux = A.copy()
    A = A.copy()

    mergesort(A, aux, 0, len(A) - 1, count)
    
    return count

A = [2, 7, 5, 3, 0, 8, 1]
count = surpasser(A)
for v in A:
    print(count.get(v, 0))

