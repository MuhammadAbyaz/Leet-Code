def subArray(nums: list[int], k):
    lo, hi, cnt, total, n = 0, 0, 0, 0, len(nums)
    while hi < n:
        total += nums[hi] % 2
        while total > k:
            total -= nums[lo] % 2
            lo += 1
        cnt += hi - lo + 1
        hi += 1
    return cnt


def numberOfSubarrays(nums: list[int], k: int) -> int:
    return subArray(nums, k) - subArray(nums, k - 1)


print(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
