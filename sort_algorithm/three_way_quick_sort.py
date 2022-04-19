def partition(arr, fist, last, start, mid):
    pivot = arr[last]
    end = last

    while mid[0] <= end:
        if arr[mid[0]] < pivot:
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]

            mid[0] = mid[0] +1
            start[0] = start[0] + 1

        elif arr[mid[0]] > pivot:
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]

            end = end -1
        else:
            mid[0] = mid[0] + 1


def quicksort(arr, first ,last):
    if first >= last:
        return
    
    if last == first + 1:
        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]
            return

    start = [first]
    mid = [first]

    partition(arr, first, last, start, mid)
    quicksort(arr, first, start[0] -1)
    quicksort(arr, mid[0], last)

arr = [4,9,4,4,1,9,4,4,9,4,4,1,4]
quicksort(arr, 0, len(arr) - 1)
print(arr)

