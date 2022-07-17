from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices

        self.graph = defaultdict(list)

        self.tc = [[0 for j in range(self.V)] for i  in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def DFSUtil(self, s, v):
        if (s==v):
            if (v in self.graph[s]):
                self.tc[s][v] = 1
        else:
            self.tc[s][v] = 1

        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                if s==i:
                    self.tc[s][i] = 1
                else:
                    self.DFSUtil(s, i)

    def transitiveClosure(self):
        for i in range(self.V):
            self.DFSUtil(i, i)
        print(self.tc)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.transitiveClosure()


