from typing import List


# def maximumImportance(n: int, roads: List[List[int]]) -> int:
#     connections = [0] * n
#     for road in roads:
#         connections[road[0]] += 1
#         connections[road[1]] += 1
#     cities = list(range(n))
#     cities.sort(key=lambda x: -connections[x])
#     res = 0
#     for i in range(n):
#         res += (n - i) * connections[cities[i]]
#     return res
def maximumImportance(n: int, roads: List[List[int]]) -> int:
    connections: dict = {}
    for road in roads:
        connections[road[0]] = connections.get(road[0], 0) + 1
        connections[road[1]] = connections.get(road[1], 0) + 1
    connections = dict(
        sorted(connections.items(), key=lambda item: item[1], reverse=True)
    )
    res = 0
    cnt = 0
    for val in connections:
        res += (n - cnt) * connections[val]
        cnt += 1
    return res


roads = [[0, 3], [2, 4], [1, 3]]
print(maximumImportance(5, roads))
