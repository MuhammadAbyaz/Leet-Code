def getRow(self, rowIndex: int):
    triangle = [[1] for _ in range(rowIndex + 1)]
    if rowIndex == 0:
        return triangle[rowIndex]
    triangle[1].append(1)
    for i in range(1, len(triangle) - 1):
        j = 0
        k = 1
        while k < len(triangle[i]):
            triangle[i + 1].append(triangle[i][j] + triangle[i][k])
            j += 1
            k += 1
        triangle[i + 1].append(1)
    return triangle[rowIndex]
