from itertools import combinations
from typing import List


def smallestDistancePair(nums: List[int], k: int) -> int:
    res = list(combinations(nums, 2))
    diff = []
    for val in res:
        diff.append(abs(val[0] - val[1]))
    diff.sort()
    return diff[k - 1]


print(smallestDistancePair([1, 3, 1], 1))
