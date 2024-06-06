import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)

    def sufficientSpeed(count):
        return sum(math.ceil(i / count) for i in piles) <= h

    while l < r:
        mid = l + (r - l) // 2
        if sufficientSpeed(mid):
            r = mid
        else:
            l = mid + 1
    return l
