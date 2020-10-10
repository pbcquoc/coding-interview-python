"""
 Given an array of N distinct integers, find floor value of input 'key'. Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome.
"""

def floor(arr, l, r, key):
    while r - l > 1:
        m = (l+r)//2
        if arr[m] <= key:
            l = m
        else:
            r = m

    if arr[r] == key:
        return arr[r]
    else:
        return arr[l]  

arr = [1,2,5,6,7,9,10]
key = 10
r = floor(arr, 0, len(arr)-1, key)
print(r)
