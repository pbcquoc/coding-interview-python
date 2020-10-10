"""
Given a sorted array with possible duplicate elements. Find number of occurrences of input ‘key’ in log N time.
"""

def find_right(arr, l, r, key):
    while r - l > 1:
        m = (l+r)//2
        if key < arr[m]:
            r = m 
        else:
            l = m

    if arr[l] == key:
        return l
    elif arr[r] == key:
        return r
    else:
        return -1

def find_left(arr, l, r, key):
    while r - l > 1:
        m = (l+r)//2
        if key <= arr[m]:
            r = m
        else:
            l =m 

    if arr[l] == key:
        return l
    elif arr[r] == key:
        return r
    else:
        return -1

arr = [1,1,2,3,3,4,5,5,7,9]
key = 3

l = find_left(arr, 0, len(arr)-1, key)
r = find_right(arr, 0, len(arr)-1, key)
print(r - l + 1)
