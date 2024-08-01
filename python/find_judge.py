from typing import List
def findJudge(n: int, trust: List[List[int]]) -> int:
    parent = [0 for _ in range(n)]
    child = [0 for _ in range(n)]
    for edge in trust:
        parent[edge[1] - 1] += 1
        child[edge[0] -1] += 1
    for i in range(len(parent)):
        if parent[i] == n - 1 and not child[i]:
            return i+1
    return -1


print(findJudge(3,[[1,3],[2,3],[3,1]]))
