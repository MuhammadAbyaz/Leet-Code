def checkMax(grid, indices, direction, maxValue):
    if indices[1] < len(grid[0]) and indices[0] < len(grid):
        for val in direction:
            if indices[0] == 0 and val == [-1, 0]:
                continue
            if (indices[1] + val[1]) == len(grid[0]) and val == [0, 1]:
                continue
            if (indices[0] + val[0]) == len(grid) and val == [1, 0]:
                continue
            if indices[1] == 0 and val == [0, -1]:
                continue
            if grid[indices[0] + val[0]][indices[1] + val[1]] >= maxValue:
                return False
    return True


def numCells(grid):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    count = 0
    for i in range(len(grid)):
        maxValue = max(grid[i])
        for j in range(len(grid[0])):
            if grid[i][j] == maxValue:
                if checkMax(grid, [i, j], directions, maxValue):
                    count += 1
                    break
    return count


print(numCells([[9, 1, 1], [1, 1, 9], [9, 1, 1], [1, 1, 1]]))
