# Graphs

A modular graph-practice roadmap, from traversal basics to advanced graph
algorithms. Keep each solution focused on one idea; add problem-specific
solutions beside the relevant topic as practice grows.

## Roadmap

| Folder | Topics to cover |
| --- | --- |
| `01_Basics` | Adjacency lists, DFS, BFS, connected components, flood fill |
| `02_Grid` | Grid traversal, islands, boundary traversal, multi-source BFS |
| `03_Cycle_Bipartite` | Cycle detection in directed/undirected graphs, bipartite coloring |
| `04_Topological_Sort` | Kahn's algorithm, DFS ordering, DAG prerequisites |
| `05_Shortest_Path` | BFS on unweighted graphs, Dijkstra, Bellman-Ford, DAG paths, Floyd-Warshall |
| `06_DSU` | Disjoint Set Union, path compression, union by size/rank |
| `07_MST` | Kruskal, Prim, minimum spanning trees |
| `08_Advanced` | Bridges, articulation points, SCCs, Euler paths, advanced problems |

## Representation

For most LeetCode problems, an adjacency list is the default: `adj[u]` stores
the neighbors reachable from vertex `u`. It uses `O(V + E)` space and supports
linear-time traversal. For an undirected graph, add both `u -> v` and `v -> u`.
For a directed graph, add only the given direction. A matrix uses `O(V^2)` space
and is useful when the graph is dense or edge lookup must be constant time.

The starter files use zero-based vertex IDs and an adjacency list. Each
traversal visits only the component reachable from its start vertex. To handle
all components, loop over every vertex and start another traversal whenever
it is still unvisited.

## Traversal templates

### DFS

Use DFS for reachability, components, flood fill, and exploring all paths or
states. The C++ starter uses an explicit stack, avoiding recursion-depth limits.
The Python starter also uses an explicit stack. Mark vertices when pushing
them, so the same vertex is not queued repeatedly.

### BFS

Use BFS for level order and shortest paths in an unweighted graph. It explores
vertices in increasing number of edges from the start. Mark a vertex visited
when enqueuing it. In Python, use `collections.deque`; removing from the front
of a list is linear time.

## Complexity notes

| Algorithm / representation | Time | Extra space |
| --- | --- | --- |
| Build adjacency list | `O(V + E)` | `O(V + E)` |
| DFS over one component | `O(V + E)` worst case | `O(V)` |
| BFS over one component | `O(V + E)` worst case | `O(V)` |
| Visit all components | `O(V + E)` | `O(V)` visited state |
| Adjacency matrix | edge lookup `O(1)`; scan neighbors `O(V)` | `O(V^2)` |

`V` is the number of vertices and `E` is the number of edges. For undirected
graphs, each edge normally appears twice in the adjacency list; this does not
change the asymptotic bounds.

## Common mistakes

- Forgetting to mark a vertex visited, or marking it only after removing it
  from the queue/stack and allowing duplicates to accumulate.
- Traversing from one start vertex and assuming that covers a disconnected
  graph.
- Adding only one direction for an undirected edge, or adding both directions
  for a directed edge.
- Using DFS to find an unweighted shortest path. Use BFS when each edge has
  equal cost.
- Using Dijkstra when negative-weight edges are possible; use Bellman-Ford or
  a suitable DAG algorithm instead.
- Confusing number of vertices with the largest vertex label. If labels are
  not dense from zero, map them to indices or use an appropriate data
  structure.
- Reusing stale `visited`, distance, or parent state between test cases.
- Treating a grid as an ordinary graph without checking row/column bounds and
  whether a cell is blocked or already visited.
- Assuming one traversal order is unique. DFS/BFS order depends on neighbor
  ordering unless the problem specifies a tie-breaking rule.

## LeetCode workflow

1. Identify whether the input is a graph, a grid, or a graph that must be
   constructed from prerequisites/edges.
2. Decide whether edges are directed, weighted, or unweighted, and whether the
   graph can be disconnected.
3. Choose a representation and traversal/algorithm based on the required
   output, then state its time and space complexity.
4. Test a single vertex, a disconnected graph, a cycle, and any important
   boundary case for the problem.

The `.cpp` and `.py` files in `01_Basics` are runnable examples. For LeetCode,
copy the traversal function into the required `Solution` method and adapt the
input representation and return type.
