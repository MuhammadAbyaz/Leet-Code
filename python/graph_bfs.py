from typing import List
from collections import deque

def bfsOfGraph(V:int, adj:List[List[int]])->List[int]:
    q = deque()
    graph = []
    visited = [0 for _ in range(V)]
    visited[0] = 1
    q.append(0)
    while q:
        current = q.popleft()
        graph.append(current)
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                q.append(neighbor)
    return graph

print(bfsOfGraph(4,[[1],[2,3],[0],[]]))
