def minSubArrayLen(target: int, nums: list[int]):
    lo = 0
    res = float("inf")
    total = 0
    for hi in range(len(nums)):
        total += nums[hi]
        while total >= target:
            res = min(res, (hi - lo) + 1)
            total -= nums[0]
            lo += 1
    return res if res != float("inf") else 0


print(
    minSubArrayLen(
        7,
        [2, 3, 1, 2, 4, 3],
    )
)
