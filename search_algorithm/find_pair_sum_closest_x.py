"""
cho một dãy được sắp sếp, tìm 2 số sao cho tổng gần x cho trước nhất
- 
"""
def closest_pair(arr, x):
    l, r = 0, len(arr) - 1
    diff = 99999

    while l < r:
        if abs(arr[l] + arr[r] - x) < diff:
            rs_l = l
            rs_r = r
            diff = abs(arr[l] + arr[r] - x)

        if (arr[l] + arr[r] > x):
            r -= 1
        else:
            l += 1
    
    return arr[rs_l], arr[rs_r]
arr = [10, 22, 28, 29, 30, 40]
x = 54
print(closest_pair(arr, x))
