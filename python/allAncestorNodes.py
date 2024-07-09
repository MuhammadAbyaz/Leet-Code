def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    def dfs(graph, parent, curr, res, visit):
        visit[curr] = True
        for dest in graph[curr]:
            if not visit[dest]:
                res[dest].append(parent)
                dfs(graph, parent, dest, res, visit)

    res: list[list[int]] = [[] for _ in range(n)]
    graph: list[list[int]] = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    for i in range(n):
        dfs(graph, i, i, res, [False] * n)
    for i in range(n):
        res[i].sort()
    return res


print(
    getAncestors(
        8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    )
)
