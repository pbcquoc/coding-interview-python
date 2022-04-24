def smallest_diff_pair(a, b):
    a.sort()
    b.sort()

    i=j=0
    
    result = 99999
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < result:
            result = abs(a[i] - b[j])

        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    return result

a = [1, 2, 11, 5]
b = [4, 12, 19, 23, 127, 235]

print(smallest_diff_pair(a, b))

