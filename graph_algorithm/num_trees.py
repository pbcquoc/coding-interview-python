def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def DFSUtil(u, adj, visited):
    visited[u] = True

    for i in range(len(adj[u])):
        if visited[adj[u][i]] == False:
            DFSUtil(adj[u][i], adj, visited)

def countTrees(adj, V):

