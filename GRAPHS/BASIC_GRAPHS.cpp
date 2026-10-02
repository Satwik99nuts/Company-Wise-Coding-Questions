#include <iostream>
#include <vector>

int main() {
    const int n = 2;
    std::vector<std::vector<int>> graph(n, std::vector<int>(n, 0));

    // Add an undirected edge between vertices 0 and 1.
    graph[0][1] = 1;
    graph[1][0] = 1;

    for (const auto& row : graph) {
        for (int edge : row)
        {
            std::cout << edge << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}
