def noble_integer(arr, n):
    arr.sort()

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            continue

        if arr[i] == n - i - 1:
            return arr[i]
    
    if arr[n-1] == 0:
        return 0
    
    return -1

def noble_integer(arr, n):
    count = [0]*(n+1)

    for i in range(n):
        if arr[i] < 0:
            continue
        elif arr[i]>=n:
            count[n] += 1
        else:
            count[arr[i]] += 1
    
    total_greater = count[n]
    for i in range(n-1, -1, -1):
        if total_greater == i and count[i] > 0:
            return i
        
        elif total_greater > i:
            return -1
        total_greater += count[i]

    return -1

arr = [10, 3, 20, 40, 2]
print(noble_integer(arr, len(arr)))
