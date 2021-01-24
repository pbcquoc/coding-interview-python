"""
Tìm 3 phần tử lớn nhất trong dãy
"""
def three_largest(arr):
    first=second=third = -999999
    for x in arr:
        if (x > first):
            third = second
            second=first
            first = x
        elif (x > second):
            third = second
            second = x
        elif (x > third):
            third = x

    return first, second, third

arr = [12, 13, 1, 10, 34, 1] 

print(three_largest(arr))
