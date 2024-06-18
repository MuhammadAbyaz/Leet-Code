from itertools import product


def minPatches(nums: list[int], n: int) -> int:
    patches = 0
    cnt = 1
    lo = 0
    size = len(nums)
    while cnt <= n:
        if lo < size and nums[lo] <= cnt:
            cnt += nums[lo]
            lo += 1
        else:
            patches += 1
            cnt += cnt
    return patches


print(
    minPatches(
        [
            1,
            2,
            16,
            19,
            31,
            35,
            36,
            64,
            64,
            67,
            69,
            71,
            73,
            74,
            76,
            79,
            80,
            91,
            95,
            96,
            97,
        ],
        8,
    )
)
