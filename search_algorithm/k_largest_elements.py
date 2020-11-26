"""
tìm k phần tử lớn nhất
cách 1:
    modify  bubble sort để chỉ cần chạy k lần
cách 2: sử dụng tmp_arr lưu lại k phần từ đầu, 
        - tính min của tmp_arr 
        - so sánh phần tử từ k đến n với min
        - nếu phần từ i lớn hơn min, thay arr[i] vào vị trí min 
cách 3:
    - sort array
    - lấy k phần tử lớn nhất
"""

def bubble_k_time(arr, k):
    for i in range(k):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr[-k:]

def temporary_arr(arr, k):
    temp_arr = arr[:k]
    min_idx = temp_arr.index(min(temp_arr))

    for i in range(k, len(arr)):
        if arr[i] > temp_arr[min_idx]:
            temp_arr[min_idx] = arr[i]
            min_idx = temp_arr.index(min(temp_arr))
    
    return temp_arr



arr = [1, 23, 12, 9, 30, 2, 50] 
k = 3
print(bubble_k_time(arr, k))
print(temporary_arr(arr, k))
