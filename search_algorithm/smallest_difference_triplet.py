"""
Cho 3 dãy, tìm bộ 3 số x, y, z sao cho mỗi số đến từ 3 dãy và có max(x, y, z) - min(x, y, z) nhỏ nhất
Solution:
    Sort 3 dãy
    rồi dùng 3 pointers 
"""
def smallest_diff_triplet(arr1, arr2, arr3):
    arr1.sort()
    arr2.sort()
    arr3.sort()

    res_min, res_max, res_mid = 0, 0, 0

    i, j, k = 0, 0, 0 
    diff = 99999

    while (i < len(arr1) and j < len(arr2) and k < len(arr3)):
        s = arr1[i] + arr2[j] + arr3[k]
        maximum = max(arr1[i], arr2[j], arr3[k])
        minimum = min(arr1[i], arr2[j], arr3[k])
        
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1
        
        if diff > (maximum - minimum):
            diff = maximum - minimum
            res_max = maximum
            res_min = minimum
            res_mid = s - (maximum + minimum)
            
    return res_max, res_mid, res_min

arr1 = [5, 2, 8] 
arr2 = [10, 7, 12] 
arr3 = [9, 14, 6] 
print(smallest_diff_triplet(arr1, arr2, arr3))
