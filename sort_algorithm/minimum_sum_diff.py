def min_sum(a, b, n):
    a.sort()
    b.sort()
    
    s = 0
    for i in range(n):
        s += abs(a[i] - b[i])
    
    return s

a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
print(min_sum(a, b, len(a)))
