def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for val in matrix:
        lo = 0
        hi = len(val) - 1
        if target > val[hi]:
            continue
        else:
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if val[mid] == target:
                    return True
                elif val[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
    return False


print(searchMatrix([[1]], 1))
