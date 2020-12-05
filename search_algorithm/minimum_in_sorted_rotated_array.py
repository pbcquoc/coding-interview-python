"""
Tìm phần tử nhỏ nhất trong một dãy số được sắp xếp bị xoay ở vị trí chưa biết.
Dãy số có thể chứa các phần tử bị lặp
"""

def binary_search(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l+r)//2
        if arr[m] > arr[r]:
            l = m + 1
        elif arr[m] < arr[r]:
            r = m
        else:
            r -= 1

    return arr[l]

arr = [2,2,2,0,1]
print(binary_search(arr))
