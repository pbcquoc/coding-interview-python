"""
Tìm phần tử xuất hiện một lần duy nhất trong dãy đã sắp xếp
"""


def search(arr, low, high):
    if high < low:
        return
    if high==low:
        return arr[high]

    mid = (low + high)//2

    if mid % 2 ==0:
        if arr[mid] == arr[mid+1]:
            return search(arr, mid+2, high)
        else:
            return search(arr, low, mid)
    else:
        if arr[mid] == arr[mid -1]:
            return search(arr, mid+1, high)
        else:
            return search(arr, low, mid-1)


arr = [1, 1, 2, 4, 4, 5, 5, 6, 6]
 
# Function call
result = search(arr, 0, len(arr)-1)
print(result)
