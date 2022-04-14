def zero_sum(arr, n):
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = - (arr[i] + arr[j])
            if x in s:
                print(arr[i], arr[j], x)
            else:
                s.add(arr[j])

def zero_sum(arr, n):
    arr.sort()

    for i in range(n-1):
        l = i+1
        r = n-1
        x = arr[i]

        while l < r:
            if x + arr[l] + arr[r] == 0:
                print(x, arr[r], arr[l])
                l += 1
                r -= 1
            elif x + arr[l] + arr[r] < 0:
                l += 1
            else:
                r -= 1


arr = [0, -1, 2, -3, 1]
print(zero_sum(arr, len(arr)))
