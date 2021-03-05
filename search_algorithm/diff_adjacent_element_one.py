"""
tìm một phần tử x cho trước trong một mảng khi biết diff giữa 2 phần tử kế nhau luôn là 1
Solution:
    Bắt đầu từ bên trái, so sánh phần tử hiện tại với x, mỗi lần jump một khoảng bằng diff của phần tử hiện tại vơi x, vì chúng ta biết rằng phần tử x phải ở vị trí ít nhất cách phần tử hiện tại là diff.
"""
def search(arr, x):
    i = 0
    while i < len(arr):
        if arr[i] == x:
            return i

        i = i + abs(arr[i] - x)
    return -1

arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3 ] 
x = 3
print(search(arr, x))
