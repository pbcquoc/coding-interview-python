def fillHeight(p, node, visited, height):
    if p[node] == -1:
        visited[node] = 1
        return 0

    if visited[node]:
        return height[node]
    
    visited[node] = 1
    height[node] = 1 + fillHeight(p, p[node], visited, height)

    return height[node]

def findHeight(parent, n):
    ma = 0

    visited = [0]*n
    height = [0]*n

    for i in range(n):
        if not visited[i]:
            height[i] = fillHeight(parent, i, visited, height)

            ma = max(ma, height[i])


    return ma

parent = [-1, 0, 0, 0, 3, 1, 1, 2]
n = len(parent)

print("Height of N-ary Tree =", findHeight(parent, n))
