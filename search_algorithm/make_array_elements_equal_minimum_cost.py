"""
Cho một dãy, cần làm cho các số trong dãy bằng nhau với minimum cost, cost được tính bằng tổng abs(x-y)
https://www.geeksforgeeks.org/make-array-elements-equal-minimum-cost/
Solution:
    Hàm cost có dạng unimodal function, kiểu U-shape, Do đó có thể dùng ternary search để tìm maximum or minimum 
"""
def cost(arr, x):
    c = 0
    for e in arr:
        c += abs(x- e)

    return c

def minimum_cost(arr):
    high, low = max(arr), min(arr)
    while(high - low > 2):
        m1 = low + (high-low)//3
        m2 = high - (high-low)//3

        cost1 = cost(arr, m1)
        cost2 = cost(arr, m2)
        
       
        if cost1 < cost2:
            high = m2
        else:
            low = m1
        
        print(high, low)

    return cost(arr, (low+high)//2)

arr = [1, 100, 101]

print(minimum_cost(arr))
