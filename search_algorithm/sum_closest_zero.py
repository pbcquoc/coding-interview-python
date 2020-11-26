def min_abs_pair(arr, l , r):
    min_s = abs(arr[0] + arr[-1])
    res_l, res_r = l, r

    while l < r:
        s = abs(arr[l] + arr[r])
        if s < min_s:
            min_s = s
            res_l = l
            res_r = r

        if s > 0:
            r -= 1
        else:
            l += 1

    return arr[res_l], arr[res_r]

arr = [1, 60, -10, 70, -80, 85]  
arr = sorted(arr)
print(min_abs_pair(arr, 0, len(arr)-1))
