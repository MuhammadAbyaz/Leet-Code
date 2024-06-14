def maxRunTime(n: int, batteries: list[int]) -> int:
    lo = 1
    hi = sum(batteries) // 2
    batteries.sort()
    while lo < hi:
        mid = hi - (hi - lo) // 2
        total = sum(min(battery, mid) for battery in batteries)
        if total >= mid * n:
            lo = mid
        else:
            hi = mid - 1
    return lo


print(maxRunTime(2, [1, 1, 1, 1]))
