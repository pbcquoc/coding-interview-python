"""
Cho dãy số, tìm tổng 3 số bằng 0
https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
Solution:Dựa trên bài toán tìm tổng 2 số bằng 0
"""

def zero_triplet(arr):
    arr.sort()

    for i in range(0, len(arr) -1):
        l = i + 1
        r = len(arr) - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r]==0):
                l += 1
                r -= 1
                print(x, arr[l], arr[r])

            if (x + arr[l] + arr[r] < 0):
                l += 1
            else:
                r -= 1


arr = [0, -1, 2, -3, 1]
zero_triplet(arr)
