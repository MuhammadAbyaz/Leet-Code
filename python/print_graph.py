from typing import List
def printGraph(V : int, edges : List[List[int]]) -> List[List[int]]:
    graph = [[] for _ in range(V)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

print(printGraph(5,[(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)]))

