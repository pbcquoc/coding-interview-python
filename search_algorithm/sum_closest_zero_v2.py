"""
tìm tổng 2 số gần bằng zero nhất ?
sau khi sort dãy số arr theo abs, 
tổng 2 số liên tiếp nhỏ nhất chính là 2 số cần tìm tại vì sau khi sort theo abs xong, giả sử số abs(a[0] + a[1]) sẽ luôn nhỏ hơn abs(a[0]) + a[2]), abs(a[0] + a[3]),.. do đó tại mỗi i chỉ cần xét 2 số liên tiếp
"""
def closest_zero(arr):
    min_s = abs(arr[0] + arr[1])
    res_l, res_r = 0, 1

    for i in range(1, len(arr)):
        s = abs(arr[i] + arr[i-1])
        if s < min_s:
            min_s = s
            res_l = i-1
            res_r = i

    return arr[res_l], arr[res_r]

arr = [-1, 1, 60, -10, 70, -80, 85]
arr = sorted(arr, key=lambda x: abs(x))

print(closest_zero(arr))
