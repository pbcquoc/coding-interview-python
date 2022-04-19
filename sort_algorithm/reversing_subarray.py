def check_reverse(arr, n):
    tmp = sorted(arr)

    for front in range(n):
        if arr[front] != tmp[front]:
            break

    for back in range(n-1, -1, -1):
        if arr[back] != tmp[back]:
            break
    
    if front >= back:
        return True

    while front != back:
        front += 1
        if arr[front - 1] < arr[front]:
            return False

    return True

def check_reverse(arr, n):
    if n == 1:
        return True

    i = 1
    for i in range(1, n):
        if arr[i -1] < arr[i]:
            if i == n:
                return True
        else:
            break
    print(i) 
    j = i
    while j < n and arr[j] < arr[j-1]:
        if i > 1 and arr[j] < arr[i-2]:
            return False
        j+=1
        if j==n:
            return True
    print(i, j)
    k = j
    if arr[k] < arr[i-1]:
        return False

    while k > 1 and k < n:
        if arr[k] < arr[k -1]:
            return False
        k += 1

    return True
arr = [1,2,3,4,20,9,16,17]
print(check_reverse(arr, len(arr)))
