"""
https://www.geeksforgeeks.org/find-largest-multiple-3-array-digits-set-2-time-o1-space/
"""
MAX_SIZE = 10
def counting_sort(arr, n):
    count = [0]*MAX_SIZE
    for i in range(n):
        count[arr[i]] += 1
    
    index = 0
    for i in range(MAX_SIZE):
        while count[i] > 0:
            arr[index] = i
            count[i] -= 1
            index += 1

arr = [4, 4, 1, 1, 1, 3]
counting_sort(arr, len(arr))
print(arr)
