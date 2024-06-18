def triangleNumber(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    valid = 0
    for hi in range(2, n):
        l = 0
        r = hi - 1
        while l < r:
            if nums[l] + nums[r] > nums[hi]:
                valid += r - l
                r -= 1
            else:
                l += 1
    return valid


print(triangleNumber([2, 3, 4, 4]))
