"""
Given a sorted array of distinct elements, and the array is rotated at an unknown position. Find minimum element in the array.
"""

def minimun(arr, l, r):
    while r - l > 1:
        m = (l+r)//2
        if arr[m] > arr[r]:
            l = m
        elif arr[m] < arr[l]:
            r = m
        print(arr[l:r])

    return arr[r]

arr = [4,6,8,1,2,3]
r = minimun(arr, 0, len(arr)-1)
print(r)
