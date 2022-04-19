"""
Liên tục chọn phần từ nhỏ nhất và đặt ở vị trí đầu tiên 
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    

A = [64, 25, 12, 22, 11]
selection_sort(A)
print(A)
