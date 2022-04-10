from math import sqrt

def greatest_product(arr, n):
    m = {}
    for i in arr:
        m[i] = m.get(i, 0) + 1

    arr.sort()

    for i in range(n-1, 0, -1):
        j = 0
        while j < i and arr[j] <= sqrt(arr[i]):
            if arr[i] % arr[j] == 0:
                result = arr[i]//arr[j]
                
                if result != arr[j]:
                    if result in m and m[result] > 0:
                        return arr[i]
                else:
                    if result in m and m[result] > 1:
                        return arr[i]

    return -1

arr = [17, 2, 1, 15, 30]
print(greatest_product(arr, len(arr)))
