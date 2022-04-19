def overlap_interval(arr):
    max_ele = 0
    for start, end in arr:
        if max_ele  < end:
            max_ele = end
    
    aux = [0]*(max_ele+1)
    for start, end in arr:
        aux[start] += 1
        aux[end] -=1
        
    for i in range(1, max_ele+1):
        aux[i] += aux[i-1]

        if aux[i] >= 1:
            return True


arr = [[ 6, 8 ], [1, 3 ], [ 2, 4 ], [ 4, 7 ]]
print(overlap_interval(arr))
