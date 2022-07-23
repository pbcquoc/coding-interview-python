MAX = 100

def dfs(n, m, visit, adj, N, M):
    visit[n][m] = 1

    if n + 1 < N and adj[n][m] >= adj[n+1][m] and not visit[n+1][m]:
        dfs(n+1, m, visit, adj, N, M)

    if m + 1 < M and adj[n][m] >= adj[n][m+1] and not visit[n][m+1]:
        dfs(n, m+1, visit, adj, N, M)

    if n - 1 >= 0 and adj[n][m] >= adj[n-1][m] and not visit[n-1][m]:
        dfs(n-1, m, visit, adj, N, M)

    if m - 1 >= 0 and adj[n][m] >= adj[n][m-1] and not visit[n][m-1]:
        dfs(n, m-1, visit, adj, N, M)


def printMinSources(adj, N, M):
    x = []

    for i in range(N):
        for j in range(M):
            x.append([adj[i][j], [i, j]])

    x.sort()

    visit = [[False for i in range(MAX)] for i in range(N)]
    
    for i in range(len(x) - 1, -1, -1):
        if not visit[x[i][1][0]][x[i][1][1]]:
            print('{} {}'.format(x[i][1][0], x[i][1][1]))

            dfs(x[i][1][0], x[i][1][1], visit, adj, N, M)

N = 2
M = 2

adj = [ [ 3, 3 ], [ 1, 1 ] ]

printMinSources(adj, N, M)

