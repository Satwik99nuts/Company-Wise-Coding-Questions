# for an undirected graph
from collections import deque

def bfs(adj, src=0):
    visited = [False] * len(adj)  # Is list se pata chalega ki kaunsa node visit ho chuka hai.
    order = []  # BFS traversal ka final order yahan store hoga.
    queue = deque([src])  # Source node ko queue mein daal kar shuru karte hain.
    visited[src] = True  # Queue mein daalte hi visited mark kar do, taaki duplicate na aaye.

    while queue:
        node = queue.popleft()  # Queue se sabse pehle aaya hua node nikaalo.
        order.append(node)  # Is node ko traversal mein add karo.

        for neighbour in adj[node]:  # Current node ke saare neighbours check karo.
            if not visited[neighbour]:
                visited[neighbour] = True  # Queue mein daalne se pehle visited mark karo.
                queue.append(neighbour)

    return order


def add_edge(adj, u, v):
    adj[u].append(v)  # Undirected graph mein edge dono taraf add hoti hai.
    adj[v].append(u)


if __name__ == "__main__":
    # Example graph: 0 ke neighbours 1 aur 2 hain.
    adj = [[] for _ in range(5)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)

    print("BFS Traversal:", bfs(adj, 0))
    # Output: BFS Traversal: [0, 1, 2, 3, 4]