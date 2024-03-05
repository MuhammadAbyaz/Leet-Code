def generate(numRows):
    triangle = [[1] for _ in range(numRows)]
    if numRows == 1:
        return triangle
    triangle[1].append(1)
    if numRows == 2:
        return triangle
    for i in range(1, len(triangle) - 1):
        j = 0
        k = 1
        while k < len(triangle[i]):
            triangle[i + 1].append(triangle[i][j] + triangle[i][k])
            j += 1
            k += 1
        triangle[i + 1].append(1)
    return triangle


print(generate(5))
