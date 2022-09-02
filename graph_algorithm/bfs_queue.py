import queue

def addEdge(g, u, v):
    g[u].append(v)
    g[v].append(u)

def BFSSingleSource(g, s):
    q = queue.Queue()

    q.put(s)

    d[s] = 0
    colour[s] = 'green'

    while(not q.empty()):
        u = q.get()

        print(u, end=' ')

        i = 0
        while i < len(g[u]):
            if colour[g[u][i]] == 'white':
                colour[g[u][i]] = 'green'
                d[g[u][i]] = d[u] + 1
                p[g[u][i]] = u

                q.put(g[u][i])

            i += 1
        
        colour[u] = 'dark_green'

def BFSFull(g, n):
    
    colour = ['white']*n
    d = [0]*n
    p = [-1]*n

    for i in range(n):
        if colour[i] == 'white':
            BFSSingleSource(g, i)

n = 7
colour = [None] * n
d = [None] * n
p = [None] * n

# The Graph vector
g = [[] for i in range(n)]

addEdge(g, 0, 1)
addEdge(g, 0, 2)
addEdge(g, 1, 3)
addEdge(g, 1, 4)
addEdge(g, 2, 5)
addEdge(g, 2, 6)

BFSFull(g, n)

