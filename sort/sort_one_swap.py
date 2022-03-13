def sort(arr, n):
    
    for i in range(1, n):

        if arr[i] < arr[i-1]:

            j = i - 1
            while j >= 0 and arr[i] < arr[j]:
                j -= 1

            arr[i], arr[j+1] = arr[j+1], arr[i]


arr = [ 10, 30, 20, 40, 50, 60, 70 ]
sort(arr, len(arr))
print(arr)
