"""
https://www.geeksforgeeks.org/check-possible-sort-array-conditional-swapping-adjacent-allowed/
"""
def possible_sort(arr, n):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            if arr[i] - arr[i+1] == 1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                return False
    return True

arr = [1,0,3,2]
print(possible_sort(arr, len(arr)))
