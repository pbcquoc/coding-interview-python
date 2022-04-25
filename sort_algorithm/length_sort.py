def sort(arr, n):
    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


arr = ["GeeksforGeeks", "I", "from", "am"]
sort(arr, len(arr))
print(arr)
