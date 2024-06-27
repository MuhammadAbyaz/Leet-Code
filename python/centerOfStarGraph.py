def findCenter(self, edges: list[list[int]]) -> int:
    return (
        edges[1][0]
        if edges[1][0] == edges[0][0] or edges[1][0] == edges[0][1]
        else edges[1][1]
    )
