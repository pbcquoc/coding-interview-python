def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j+1] = b[j]
            j -= 1

        b[j+1] = up
    
    return b

def bucket_sort(x):
    arr = []
    slot_num = 10

    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num*j)
        arr[index_b].append(j)

    for i in range(10):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    
    return x

print(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]))
