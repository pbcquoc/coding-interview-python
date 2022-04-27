def sort(arr, n):
    index = [0]*n
    for i in range(n):
        index[i] = i

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[index[min_index]] > arr[index[j]]:
                min_index = j

        index[min_index], index[i] = index[i], index[min_index]
    
    for i in range(n):
        print(arr[index[i]], end=" ")

arr = ["geeks", "quiz", "geeks", "for"]
sort(arr, len(arr))
