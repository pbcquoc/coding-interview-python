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

def count_pairs_with_sorting(arr, k):
    count = 0
    arr.sort()

    l, r = 0, 0
    while r >= l and r < len(arr):
        diff = arr[r] - arr[l]
        if diff == k:
            print(arr[l], arr[r])

            r += 1
            l += 1
        elif diff < k:
            r += 1
        else:
            l += 1


def binary_search(arr, x, low):
    high = len(arr)  - 1
    ans = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            high = mid -1
            ans = mid
        else:
            low = mid + 1

    return ans


def count_pairs_with_bs(arr, k):
    count = 0
    arr.sort()
    N = len(arr)
    for i in range(N):
        X = binary_search(arr, arr[i] + k, i + 1)
        if X != N:
            Y = binary_search(arr, arr[i] + k + 1, i +1)
            count += Y - X

    return count

arr = [ 1, 3, 5, 8, 6, 4, 6 ]
k = 0
print(count_pairs_with_bs(arr, k))

