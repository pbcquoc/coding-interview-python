from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def dfs_util(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


    def add_edge(self, v, w):
        self.graph[v].append(w)

    def find_mother(self):
        visited = [False]*self.V

        v = 0

        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited)
                v = i


        visited = [False]*self.V
        self.dfs_util(v, visited)

        if any(i==False for i in visited):
            return -1
        else:
            return v

g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(4, 1)
g.add_edge(6, 4)
g.add_edge(5, 6)
g.add_edge(5, 2)
g.add_edge(6, 0)

print('mother vertex: {}'.format(g.find_mother()))
