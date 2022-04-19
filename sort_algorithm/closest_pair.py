def closest_pair(arr, x):
    diff = 99999
    res_l, res_r = 0, len(arr) - 1
    l, r = 0, len(arr) - 1

    while l < r:
        if abs(arr[r] + arr[l] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[r] + arr[l] - x)

        if abs(arr[r] + arr[l]) > x:
            r -=1
        else:
            l += 1

    return res_l, res_r

arr = [10, 22, 28, 29, 30, 40]
x = 54
print(closest_pair(arr, x))
