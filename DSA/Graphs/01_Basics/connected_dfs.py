def dfs(start, graph):
    visited = set()
    order = []

    def go(node):
        visited.add(node)
        order.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                go(nxt)
    go(start)
    return order
n = 5
graph = [[] for _ in range(n)]

def add_edge(a,b):
    graph[a].append(b)
    graph[b].append(a)

add_edge(1,2)
add_edge(1,0)
add_edge(2,0)
add_edge(2,3)
add_edge(2,4)

print(*dfs(0,graph))