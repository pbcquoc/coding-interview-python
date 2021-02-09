"""
Đếm số 1 trong 1 dãy số bao gồm 0 và 1 trong một chuỗi sắp xếp theo tứ tự không tăng 
- Dùng binary search
"""
def count_ones(arr, l, r):
    while(l < r):
        m = (l+r)//2

        if arr[m] - arr[m+1] == 1:
            return m+1
        
        if arr[m] == 0:
            return count_ones(arr, l, m-1)
        else:
            return count_ones(arr, m+1, r)

arr=[1, 1, 0, 0, 0, 0, 0]
print(count_ones(arr, 0, len(arr)-1))
