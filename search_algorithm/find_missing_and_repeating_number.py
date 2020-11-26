"""
Cho n số có giá trị từ 1-n, trong đó có một số bị missing và 1 số xuất hiện 2 lần. 
Tìm 2 số đó
Cách 1: sort và tìm missing + repeating 
"""

def find_two_number(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i]

arr = [7, 3, 4, 5, 5, 6, 2] 
print(find_two_number(arr))
