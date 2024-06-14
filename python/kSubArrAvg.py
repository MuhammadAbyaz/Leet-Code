from typing import List


def getAverages(nums: List[int], k: int) -> List[int]:
    lo = 0
    n = len(nums)
    res = [-1] * n
    windowLen = 2 * k + 1
    winSum = 0
    for hi in range(n):
        winSum += nums[hi]
        if hi - lo + 1 == windowLen:
            res[lo + k] = winSum // windowLen
            winSum -= nums[lo]
            lo += 1
    return res


print(getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
