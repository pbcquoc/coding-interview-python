def rec_search(arr, l, r, key):
    if arr[l] == key:
        return l
    elif arr[r] == key:
        return r
    else:
        rec_search(arr, l+1, r-1, key)

    return -1

arr = [12, 34, 54, 2, 3] 
n = len(arr) 
x = 3
r = rec_search(arr, 0, n-1, x) 
print(r)
    
