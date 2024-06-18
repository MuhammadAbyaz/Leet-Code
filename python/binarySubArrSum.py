def subArr(nums: list[int], goal: int) -> int:
    if goal < 0:
        return 0
    lo, total, res, hi, n = 0, 0, 0, 0, len(nums)
    while hi < n:
        total += nums[hi]
        while total > goal:
            total -= nums[lo]
            lo += 1
        res += hi - lo + 1
        hi += 1
    return res


def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    return subArr(nums, goal) - subArr(nums, goal - 1)


print(numSubarraysWithSum([0, 0, 0, 0, 0], 0))
