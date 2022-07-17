from collections import deque

adj = [[] for i in range(10001)]

def addEdge(v, w):
    adj[v].append(w)
    adj[w].append(v)

def BFS(s, l):
    V = 100
    visited = [False]*V
    level = [0]*V

    queue = deque()

    visited[s] = True
    queue.append(s)
    level[s] = 0

    while len(queue) > 0:
        s = queue.popleft()

        for i in adj[s]:
            if not visited[i]:
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)

    count = 0
    for i in range(V):
        if level[i] == l:
            count += 1

    return count

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(2, 4)
addEdge(2, 5)

level = 2

print(BFS(0, level))
