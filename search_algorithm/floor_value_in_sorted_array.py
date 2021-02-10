"""
Cho một dãy số đã được sắp sếp, và số x. tìm số nằm trong dãy sao cho số đó <= x
Solution:
    dùng binary search
"""
def floor_value(arr, low, high, x):
    if x < arr[0]:
        return -1
    if x > arr[-1]:
        return arr[-1]

    while (low < high):
        m = (low + high)//2
        if arr[m] == x:
            return arr[m]
        if arr[m] < x < arr[m+1]:
            return arr[m]

        elif arr[m] < x:
            low = m
        else:
            high = m


arr = [1, 2, 4, 6, 10, 12, 14]
x = 13
rs = floor_value(arr, 0, len(arr) - 1, x)
print(rs)
