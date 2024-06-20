def canPlaceBalls(arr, mid, balls):
    cnt = 1
    n = len(arr)
    placed = arr[0]
    for i in range(1, n):
        if arr[i] - placed >= mid:
            cnt += 1
            placed = arr[i]
        if cnt >= balls:
            return True
    return False


def maxDistance(position: list[int], m: int) -> int:
    position.sort()
    lo, hi = 1, position[len(position) - 1] - position[0] // m - 1
    res = 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if canPlaceBalls(position, mid, m):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
