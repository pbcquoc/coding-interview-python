"""
Cho số N, Tìm tất các cá khả năng của tổng d số liên tiếp bằng N
https://www.geeksforgeeks.org/print-all-possible-consecutive-numbers-with-sum-n/

"""

def consecutive_sum(N):
    count = 0
    s = 1
    end = 1
    start = 1
    
    while start <= N//2:
        if s < N:
            end += 1
            s += end

        elif s > N:
            s -= start
            start += 1
        else:
            print(list(range(start, end+1)))
            s-= start
            start += 1

N = 15
consecutive_sum(N)
