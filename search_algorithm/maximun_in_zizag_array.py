"""Tìm phần tử lớn nhất trong dãy số đầu tiên là tăng sau đó thì giảm dần
"""
def binary_search(arr, l, r):
    if l == r:
        return arr[l]

    if l == r -1:
        return max(arr[l], arr[r])

    m = (l+r)//2
    
    if arr[m-1] < arr[m] > arr[m+1]:
        return arr[m]

    if arr[m] > arr[m+1]:
        return binary_search(arr, l, m)
    else:
        return binary_search(arr, m, r)

arr = [1, 3, 50, 10, 9, 7, 6] 
print(binary_search(arr, 0, len(arr)-1))
