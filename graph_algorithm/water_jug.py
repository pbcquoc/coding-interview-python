from collections import deque

def BFS(a, b, target):
    m = {}
    isSolvable = False

    path = []

    q.append((0, 0))

    while len(q) > 0:
        u = q.popleft()

        if (u[0], u[1]) in m :
            continue

        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        path.append([u[0], u[1]])

        m[(u[0], u[1])] = 1

        if u[0] == target or u[1] == target:


Jug1, Jug2, target = 4, 3, 2
BFS(Jug1, Jug2, target)
