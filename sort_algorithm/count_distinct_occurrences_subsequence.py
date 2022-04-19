def distinct_occurrence(i, j, s, t):
    if j >= len(t):
        return 1
    if i >= len(s):
        return 0
    
    if s[i]==t[j]:
        return distinct_occurrence(i+1, j + 1, s, t) + distinct_occurrence(i+1, j, s, t)

    return distinct_occurrence(i+1, j, s, t)

def distinct_occurrence_dp(s, t):
    m = len(t)
    n = len(s)

    if m > n:
        return 0

    mat = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    for i in range(1, m + 1):
        mat[i][0] = 0
    for j in range(n + 1):
        mat[0][j] = 1


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if T[i - 1] != S[j - 1]:
                mat[i][j] = mat[i][j-1]
            else:
                mat[i][j] = mat[i][j-1] + mat[i-1][j-1]
    
    return mat[m][n]


S = 'geeksforgeeks'
T = 'ge'

print(distinct_occurrence_dp(S, T))
