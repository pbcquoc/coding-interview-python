def search(arr, l, r, key):
    while l <= r:
        m = (l+r)//2
        if arr[m] == key:
            return m

        # arr[l..m] is sorted
        if arr[m] > arr[r]:
            if arr[l] <= key <= arr[m]:
                return search(arr, l, m - 1, key)
            return search(arr, m + 1, r, key)

        if arr[m] <= key <= arr[r] :
            return search(arr, m + 1, r, key)
        return search(arr, l, m - 1, key)
    return -1

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 4
i = search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 
