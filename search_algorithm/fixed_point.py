"""
Cho dãy tăng dần, tìm vị trí mà a[i] = i
"""
def binary_search(arr, l, r):
    m = (l+r)//2
    if arr[m] == m:
        return m
    
    if m < arr[m]:
        return binary_search(arr, 0, m -1)
    else:
        return binary_search(arr, m + 1, r)

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
print(binary_search(arr, 0, len(arr)-1))
