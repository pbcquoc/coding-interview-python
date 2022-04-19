"""
a * b + c = (f + e) * d
"""

def upper_bound(arr, length, value):
    low = 0
    high = length

    while low < high:
        mid = (low + high)//2
        if value >= arr[mid]:
            low = mid + 1
        else:
            high = mid
    
    return low

def lower_bound(arr, length, value):
    low = 0
    high = length
    
    while low < high:
        mid = (low + high)//2
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid 

    return low


def find_sextuplets(arr, n):
    index = 0
    rhs = [0]*(n*n*n + 1)

    for i in range(n):
        if arr[i] != 0:
            for j in range(n):
                for k in range(n):
                     rhs[index] = arr[i] * (arr[j] + arr[k])
                     index += 1

    rhs.sort()

    result = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                val = arr[i]*arr[j] + arr[k]
                result += upper_bound(rhs, index, val) - lower_bound(rhs, index, val)

    return result

arr = [2, 3]
n = len(arr)

print(find_sextuplets(arr, n))
