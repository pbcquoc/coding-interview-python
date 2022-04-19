def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j][1] == pivot[1]:
            if arr[j][2] < pivot[2]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        elif arr[j][1] < pivot[1]:
             i += 1
             arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p -1)
        quick_sort(arr, p + 1, high)

def conflict(arr, n):
    quick_sort(arr, 0, n - 1)

    for i in range(1, n):
        if arr[i][1] == arr[i -1][1]:
            if arr[i][2] < arr[i-1][2] + 5:
                j = i - 1
                while arr[i][1] == arr[j][1] and arr[i][2] <= arr[j][2] + 5 and j > 0:
                    if arr[i][3]== 'W' or arr[j][3] == 'W':
                        print(arr[i][0], arr[j][2])

                    j -= 1
arr = [
  (1, 512, 1, 'R'),
  (2, 432, 2, 'W'),
  (3, 512, 3, 'R'),
  (4, 932, 4, 'R'),
  (5, 512, 5, 'W'),
  (6, 932, 6, 'R'),
  (7, 835, 7, 'R'),
  (8, 432, 8, 'R')
]

conflict(arr, len(arr))
