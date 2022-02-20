def merge(arr, start, mid1, mid2, end):
    left_arr = arr[start:mid1]
    mid_arr = arr[mid1:mid2]
    right_arr = arr[mid2:end+1]
   
    left_arr.append(float('inf'))
    mid_arr.append(float('inf'))
    right_arr.append(float('inf'))

    ind_left, ind_mid, ind_right = 0, 0, 0
    for i in range(start, end+1):
        minimum = min(left_arr[ind_left], mid_arr[ind_mid], right_arr[ind_right])
        if minimum == left_arr[ind_left]:
            arr[i] = minimum
            ind_left += 1
        elif minimum == mid_arr[ind_mid]:
            arr[i] = minimum
            ind_mid += 1
        else:
            arr[i] = minimum
            ind_right += 1

def merge_sort(arr, start, end):
    if end - start <= 1:
        return  
    mid1 = start + (end - start)//3
    mid2 = start + 2*(end - start)//3

    merge_sort(arr, start, mid1)
    merge_sort(arr, mid1, mid2)
    merge_sort(arr, mid2, end)
    merge(arr, start, mid1, mid2, end)

    return arr

arr = [312,413,3,423,5,3,342,1,2,53]
merge_sort(arr, 0, len(arr) -1)
print(arr)
