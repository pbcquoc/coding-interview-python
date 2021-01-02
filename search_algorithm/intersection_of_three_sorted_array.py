"""
Tìm intersection của 3 dãy số đã sắp xếp
Dùng thủ tực merge producer 
"""
def find_common(arr1, arr2, arr3):
    i, j, z = 0, 0, 0
    rs = set()
    while(i < len(arr1) and j < len(arr2) and z < len(arr3)):
        if (arr1[i]==arr2[j]==arr3[z]):
            rs.add(arr1[i])
            i += 1
            j += 1
            z += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[z]:
            j += 1
        else:
            z += 1

    return rs

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(find_common(ar1, ar2, ar3))
