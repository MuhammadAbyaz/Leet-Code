from typing import List


def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    incr: int = 0
    numsLen = len(nums)
    for i in range(1, numsLen):
        if nums[i] <= nums[i - 1]:
            incr += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1
    return incr


print(minIncrementForUnique([3, 2, 1, 2, 1, 7]))
