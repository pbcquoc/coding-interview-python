"""
Tìm ceil value của x trong sorted array
Cách 1: dùng linear search, sử lý edge case khi x bé hơn phần tử nhỏ nhất, tìm phần tử a[i] <= x <= a[i+1], hoặc không tìm thấy 
Cách 2: dùng binary search 
"""

def ceil_value(arr, x, l, r):
    if arr[r] < x:
        return -1
    if arr[l] > x:
        return arr[l]

    while (r > l + 1):
        m = (l+r)//2
        if x < arr[m]:
            r = m
        else:
            l = m 

    if arr[l] == x:
        return arr[l]
    else:
        return arr[r]

def ceil_value_v2(arr, x, l, r):
    if x < arr[l]:
        return arr[l]
    if x > arr[r]:
        return -1

    m = (l+r)//2

    if arr[m]==x:
        return arr[m]

    if x < arr[m]:
        if m-1 >= l and x > arr[m-1]:
            return arr[m]
        else:
            return ceil_value_v2(arr, x, l, m-1)
    else:
        if m+1 <= r and x < arr[m+1]:
            return arr[m+1]
        else:
            return ceil_value_v2(arr, x, m+1, r)



arr = [1, 2, 8, 10, 10, 12, 19] 
x = 0
print(ceil_value(arr, x, 0, len(arr)-1))
print(ceil_value_v2(arr, x, 0, len(arr)-1))
