def get_max(arr, q):
    max_ele = 0
    for e in arr:
        max_ele = max(max_ele, e[q])

    return max_ele

def count_sort(arr, q, n):
    max_ele = get_max(arr, q)
    p = 1

    while max_ele > 0:
        count = [0]*10
        output = [[0, 0, 0] for _ in range(n)]

        for i in range(n):
            count[(arr[i][q]//p)%10] += 1
        
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            output[count[(arr[i][q]//p)%10]-1] = arr[i]
            count[(arr[i][q]//p)%10] -= 1
        
        
        for i in range(n):
            arr[i] = output[i]

        p *= 10
        max_ele = max_ele//10

def sort(arr, n):
    count_sort(arr, 0, n)
    count_sort(arr, 1, n)
    count_sort(arr, 2, n)

#arr = [[ 20, 1, 2014 ],[ 25, 3, 2010 ],[ 3, 12, 2000 ],[ 18, 11, 2000 ],[ 19, 4, 2015 ],[ 9, 7, 2005 ]]
arr = [[20, 1, 2014], [1, 4, 2015], [3, 12, 2000], [25, 3, 2010], [8, 11, 2000], [9, 7, 2005]]

sort(arr, len(arr))
print(arr)
