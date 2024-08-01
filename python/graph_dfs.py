from typing import List


def dfsOfGraph(V, adj)->List[int]:
    visited = [0 for _ in range(V)]
    graph = []

    def traverse(parent):
        graph.append(parent)
        visited[parent] = 1
        for neighbour in adj[parent]:
            if not visited[neighbour]:
                traverse(neighbour)
    traverse(0)
    return graph

print(dfsOfGraph(5,[[2,3,1],[0],[0,4],[0],[2]]))
