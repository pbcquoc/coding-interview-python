ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]

arr = [0]*len(ar1)*2

def merge():
    i, j, k = 0, 0, 0
    while i < len(ar1) and j < len(ar2):
        print(i, j, k)
        if ar1[i] < ar2[j]:
            arr[k] = ar1[i]
            i += 1
        else:
            arr[k] = ar2[j]
            j += 1
        k += 1
    
    while i < len(ar1):
        arr[k] = ar1[i]
        k += 1
        i += 1
    
    while j < len(ar2):
        arr[k] = ar2[j]
        k += 1
        j += 1
        
