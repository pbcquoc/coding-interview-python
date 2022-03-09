def count_sort(arr, n, exp):
    output = [0]*n
    count = [0]*n

    for i in range(n):
        count[(arr[i]//exp) % n] += 1
        print(arr[i], (arr[i]//exp) % n)
    for i in range(1, n):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        output[count[(arr[i]//exp) %n] - 1] = arr[i]
        count[(arr[i]//exp) %n] -= 1

    for i in range(n):
        arr[i] = output[i]


def sort(arr, n):
    count_sort(arr, n, 1)
    count_sort(arr, n, n)

arr = [40, 12, 45, 32, 33, 1, 22]
n = len(arr)
sort(arr, n)

print(arr)
