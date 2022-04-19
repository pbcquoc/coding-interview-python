"""
https://www.geeksforgeeks.org/k-th-smallest-element-removing-given-integers-natural-numbers-set-2/
"""

def k_smallest(arr, n, k):
    arr.sort()
    for i in range(n):
        if arr[i] <= k:
            k += 1
        else:
            break

    return k

arr = [1,2]
k = 3
print(k_smallest(arr, len(arr), k))
