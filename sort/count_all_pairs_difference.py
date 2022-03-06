def count_pairs(arr):
    y = {}
    for x in arr:
        if x not in y:
            y[x-3] = x
            y[x+3] = x
        else:
            yield (x, y[x])

def binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def count_pairs(arr, k):
    count = 0 
    arr.sort()

    for i in range(0, len(arr) -2):
        j = binary_search(arr, i+1, len(arr) - 1, arr[i] + k)
        if j != -1:
            count += 1
            print(arr[i], arr[j])
    
    return count

arr = [1, 5, 3, 4, 2]
k = 3
print(count_pairs(arr, k))
