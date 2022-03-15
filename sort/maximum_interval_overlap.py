def max_guest(arrl, exit, n):
    mini = min(arrl)
    maxi = max(exit)
    
    count = [0]*(maxi - mini + 1)

    for i in range(n):
        for j in range(arrl[i], exit[i]+1):
            count[j-mini] += 1

    max_ele = max(enumerate(count), key=lambda x:x[1]) 
    max_ele = (max_ele[0]+mini, max_ele[1])
    return max_ele

def max_guest(arrl, exit, n):
    arrl.sort()
    exit.sort()

    guests_in = 1
    max_guests = 1
    time = arrl[0]

    i, j = 1, 0

    while i < n and j < n:
        if arrl[i] <= exit[j]:
            guests_in += 1
            if guests_in > max_guests:
                max_guests = guests_in
                time = arrl[i]
            i += 1
        else:
            guests_in -= 1
            j += 1
    
    return time, max_guests

arrl = [1, 2, 10, 5, 5];
exit = [4, 5, 12, 9, 12];

print(max_guest(arrl, exit, len(arrl)))
