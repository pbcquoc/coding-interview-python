"""
Tìm min và max sử dụng ít so sánh nhất ?
chia dãy thì 2 nữa left và right, đệ quy tìm min, max trên 2 nữa đó. 
"""

def min_max(arr, l, r):
    if l == r:
        return arr[l], arr[r]
    elif l == r - 1:
        if arr[l] > arr[r]:
            return arr[r], arr[l]
        else:
            return arr[l], arr[r]
    else:
        m = (l+r)//2
        left_min, left_max = min_max(arr, l, m)
        right_min, right_max = min_max(arr, m + 1, r)

        return min(left_min, right_min), max(left_max, right_max)

arr = [2,3,1,6,0,0,9]

print(min_max(arr, 0, len(arr)-1))

