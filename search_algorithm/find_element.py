"""Tìm phần tử lớn hơn các phần tử phía trước và nhỏ hơn các phần tử phía sau nó
https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
Solution:
    O(n)
    dùng mảng tạo leftmax lưu giá trị lớn nhất từ đầu đến vị trí thứ i-1, và mảng tạm rightmin lưu giá trị nhỏ nhất từ cuối về trước i - 1,
    sau đó tại mỗi vị trí i trong mảng, kiểm tra xem nó có thỏa điều kiện yêu cầu hay không
"""
def find_element(arr):
    left_max = [0]*len(arr)
    left_max[0] = float('-inf')

    right_min = [0]*len(arr)
    right_min[-1] = float('+inf')
    

    for i in range(1, len(arr)):
        left_max[i] = max(left_max[i-1], arr[i-1])

    for i in range(len(arr)-2, -1, -1):
        right_min[i] = min(right_min[i+1], arr[i+1])

    for i in range(1, len(arr)-1):
        if left_max[i] < arr[i] < right_min[i]:
            return arr[i]

arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]

rs = find_element(arr)
print(rs)

