from collections import deque

# for a single connected component
def connected_bfs(adj, src, visited, res):
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
# bfs for all connected components
def bfs(adj):
    v = len(adj)
    visited = [False]*v
    res = []

    for i in range(v):
        if not visited[i]:
            connected_bfs(adj,i,visited,res)
    return res

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    v = 6
    adj = []


    for i in range(v):
        adj.append([])

    add_edge(adj,1,2)
    add_edge(adj,2,0)
    add_edge(adj,0,3)
    add_edge(adj,4,5)

    res = bfs(adj)

    for node in res:
        print(node, end="")    