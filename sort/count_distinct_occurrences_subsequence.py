def distinct_occurrence(i, j, s, t):
    if j >= len(t):
        return 1
    if i >= len(s):
        return 0
    
    if s[i]==t[j]:
        return distinct_occurrence(i+1, j + 1, s, t) + distinct_occurrence(i+1, j, s, t)

    return distinct_occurrence(i+1, j, s, t)

S = 'geeksforgeeks'
T = 'ge'

print(distinct_occurrence(0, 0, S, T))
