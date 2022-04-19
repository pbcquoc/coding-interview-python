def join(arr, left, right, l, m, r):
    for i in range(m-l+1):
        arr[i] = left[i]
    
    i+=1
    for j in range(r-m):
        arr[i+j] = right[j]

def split(arr, left, right, l, m, r):
    for i in range(m-l+1):
        left[i] = arr[i*2]

    for i in range(r-m):
        right[i] = arr[i*2+1]

def worst_case(arr, l, r):
    if l < r:
        m = (l+r)//2
        left = [0]*(m-l+1)
        right = [0]*(r-m)
        
        split(arr, left, right, l, m, r)
        worst_case(left, l, m)
        worst_case(right, m+1, r)
        
        join(arr, left, right, l, m, r)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
worst_case(arr, 0, len(arr)-1)
print(arr)
