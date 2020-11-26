"""
Tìm phần tử nhỏ nhất và nhỏ nhì ?
cách 1:
    sort rồi lấy 2 phần tử đầu 
cách 2:
    1 vòng for tìm phần tử nhỏ nhất x
    1 vòng for nữa tìm phần tử nhỏ nhất những lớn hơn x
cách 3:
    1 vòng for duy nhất, x luôn là phần từ nhỏ nhất, y  
"""

def two_smallest(arr):
    x, y = 9999, 9999
    for i in arr:
        if i < x:
            y = x
            x = i
        elif i < y:
            y = i

    return x, y

arr = [12, 13, 1, 10, 34, 2]

print(two_smallest(arr))
