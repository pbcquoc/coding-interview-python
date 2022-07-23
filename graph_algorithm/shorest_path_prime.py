import queue

class Graph:

    def __init__(self, V):
        self.V = V
        self.l = [[] for i in range(V)]


    def addedge(self, V1, V2):
        self.l[V1].append(V2)
        self.l[V2].append(V2)

    def bfs(self, in1, in2):
        visited = [0]*self.V

        que = queue.Queue()
        visited[in1] = 1
        que.put(in1)

        while not que.empty():
            p = que.queue[0]
            que.get()

            i = 0
            while i < len(self.l[p]):
                if not visited[self.l[p][i]]:
                    visited[self.l[p][i]] = visited[p] + 1
                    que.put(self.l[p][i])

                if self.l[p][i] == in2:
                    return visited[self.l[p][i]] - 1

                i += 1



        
