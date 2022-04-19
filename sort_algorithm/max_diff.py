def max_diff(arr, n):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    dist = list(freq)
    dist.sort()
    
    min_freq = n + 1
    ans = 0
    for i in dist:
        cur_freq = freq[i]
        ans = max(ans, cur_freq - min_freq)
        min_freq = min(min_freq, cur_freq)

    return ans

arr = [3, 1, 3, 2, 3, 2]

print(max_diff(arr, len(arr)))
