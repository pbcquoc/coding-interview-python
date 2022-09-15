from collections import deque

MAX = 1001

adj = [[] for i in range(MAX)]

def build_tree(arr, n):
    root_index = 0

    for i in range(n):
        if arr[i] == -1:
            root_index = i
        else:
            adj[i].append(arr[i])
            adj[arr[i]].append(i)

    return root_index

def BFS(start):
    vis = {}

    q = deque()
    max_level_reached = 0

    q.append([start, 0])

    p = []

    while len(q) > 0:
        p = q.popleft()
        vis[p[0]] = 1

        max_level_reached = max(max_level_reached, p[1])

        for i in range(len(adj[p[0]])):

            if adj[p[0]][i] not in vis:
                q.append([adj[p[0]][i], p[1] + 1])

    return max_level_reached

parent = [-1, 0, 1, 2, 3]

# Number of nodes in tree
n = len(parent)

root_index = build_tree(parent, n)
ma = BFS(root_index)

print(ma)
