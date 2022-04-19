def sort_waveform(arr, n):
    for i in range(0, n, 2):
        if i - 1 >=0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if i + 1 < n and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [10, 90, 49, 2, 1, 5, 23]
sort_waveform(arr, len(arr))
print(arr)
