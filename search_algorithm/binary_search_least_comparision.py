"""
 Given a sorted array of N distinct elements. Find a key in the array using least number of comparisons. (Do you think binary search is optimal to search a key in sorted array?)
"""
def binary_search(arr, l, r, key):
    while (r - l > 1):
        m = (l+r)//2
        if key > arr[m]:
            l = m 
        else:
            r = m

    if arr[l] == key:
        return l
    elif arr[r] == key:
        return r
    else:
        return -1

arr = [1,2]
key = 2
r = binary_search(arr, 0, len(arr) -1, key)
print(r)
