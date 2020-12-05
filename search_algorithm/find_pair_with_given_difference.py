"""
Cho một dãy chưa được sắp sếp, và số diff 
tìm một cặp sao cho difference của 2 số bằng số diff
"""

def find_pair(arr, diff):
    d = set()
    for i in range(len(arr)):
        x1 = diff + arr[i]
        x2 = arr[i] - diff
        
        if x1 not in d:
            d.add(arr[i])
        else:
            return arr[i], x1

        if x2 not in d:
            d.add(arr[i])
        else:
            return arr[i], x2
    return -1

arr = [1, 8, 30, 40, 100] 
diff = 10

print(find_pair(arr, diff))
