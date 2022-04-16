def sort(a, b, c):
    maxv = max(a, max(b, c))
    minv = -max(-a, max(-b, -c))
    midv = (a+b+c) - (maxv+minv)
    return minv, midv, maxv

a, b, c = 4, 1, 9
print(sort(a, b, c))
