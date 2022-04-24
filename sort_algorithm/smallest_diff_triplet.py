def smallest_diff_triplet(a, b, c, n):
    a.sort()
    b.sort()
    c.sort()

    res_min = 0
    res_max = 0
    res_mid = 0

    i=j=k=0

    diff = 999999999

    while i < n and j < n and k < n:
        s = a[i] + b[j] + c[k]

        maxe = max(a[i], b[j], c[k])
        mine = min(a[i], b[j], c[k])

        if mine==a[i]:
            i += 1
        elif mine == b[j]:
            j += 1
        else:
            k += 1

        if diff > maxe - mine:
            diff = maxe - mine
            res_max = maxe
            res_mid = s - maxe - mine
            res_min = mine

    return res_min, res_mid, res_max

a = [5, 2, 8]
b = [10, 7, 12]
c = [9, 14, 6]

print(smallest_diff_triplet(a, b, c, len(a)))
