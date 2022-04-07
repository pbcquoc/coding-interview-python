def minimum_swaps(a, b, n):
    n_swaps = 0
    for i in range(n):
        if a[i] != b[i]:
            n_swaps += 1

            j = b.index(a[i])
            b[i], b[j] = b[j], b[i]

    return n_swaps

def cycle_sort(b, n):
    visited = [False]*n
    ans = 0

    for i in range(n):
        if visited[i] or b[i][0] == i:
            continue
        
        j = i
        cycle_size = 0
        while not visited[j]:
            visited[j] = True
            j = b[j][0]
            cycle_size += 1
        
        ans += (cycle_size - 1)

    return ans

def minimum_swaps(a, b, n):
    mp = {}

    for i in range(n):
        mp[b[i]] = i

    for i in range(n):
        b[i] = (mp[a[i]], a[i])

    return cycle_sort(b, n)

a = [3, 6, 4, 8]
b = [4, 6, 8, 3]

print(minimum_swaps(a, b, len(a)))
