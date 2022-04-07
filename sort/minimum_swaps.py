def min_swaps(arr):
    n = len(arr)

    arrpos = [*enumerate(arr)]

    arrpos.sort(key=lambda it:it[1])

    vis = {k: False for k in range(n)}

    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][0]==i:
            continue

        j = i
        cycle_size = 0

        while not vis[j]:
            vis[j] = True

            j = arrpos[j][0]
            cycle_size += 1

        ans += (cycle_size - 1)

    return ans

def min_swaps(arr):
    n = len(arr)

    tmp = sorted(arr)
    
    ans = 0

    for i in range(n):
        if arr[i] != tmp[i]:
            ans += 1
        
            j = arr.index(tmp[i])
            arr[i], arr[j] = arr[j], arr[i]

    return ans

arr = [1, 20, 6, 4, 5]
print(min_swaps(arr))
