from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited, vDegree, k):
        visited.add(v)

        for i in self.graph[v]:
            if vDegree[v] < k:
                vDegree[i] -= 1

            if i not in visited:
                self.DFSUtil(i, visited, vDegree, k)


    def printKCores(self, k):
        visit = set()
        degree = defaultdict(int)
        
        for i in list(self.graph):
            degree[i] = len(self.graph[i])

        for i in list(self.graph):
            if i not in visit:
                self.DFSUtil(i, visit, degree, k)

        for i in list(self.graph):
            if degree[i] >= k:
                print('\n[{}]'.format(i), end=' ')

                for j in self.graph[i]:
                    if degree[j] >= k:
                        print('-> {}'.format(j), end=' ')
                
                print()

k = 3
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.printKCores(k)
