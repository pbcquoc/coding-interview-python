def cycle_sort(arr):
    writes = 0
    for cycle_start in range(0, len(arr) - 1):
        item = arr[cycle_start]
        
        pos = cycle_start
        for i in range(cycle_start + 1, len(array)):
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item==arr[pos]:
            pos += 1

        arr[pos], arr[cycle_start] = arr[cycle_start], arr[pos]




