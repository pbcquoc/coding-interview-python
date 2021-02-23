"""
có n máy, mỗi máy cần số ngày khác nhau để tao ra một sản phẩm, tìm số ngày ít nhất để tạo ra m sản phẩm khi cả n máy chạy đồng thời
https://www.geeksforgeeks.org/minimum-time-required-produce-m-items/
"""

import math

def find_items(machines, days):
    items = 0
    for m in machines:
        items += days//m
        
    return items

def min_time(machines, goal):
    min_day = goal*math.floor(min(machines)/len(machines))
    max_day = goal*math.ceil(max(machines)/len(machines))
    
    while (min_day < max_day):
        mid = (min_day + max_day)//2
        
        items = find_items(machines, mid)
        if items < goal:
            min_day = mid + 1
        else:
            max_day = mid
    
    return max_day


arr = [2, 3]
m = 5
rs = min_time(arr, m)
print(rs)
