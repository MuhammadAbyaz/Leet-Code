def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            if (v + nums[l] + nums[r]) == 0:
                li = [v, nums[l], nums[r]]
                result.append(li)
            if (v + nums[l] + nums[r]) < 0:
                l += 1
            elif (v + nums[l] + nums[r]) > 0:
                r -= 1
            else:
                l += 1
                while nums[l - 1] == nums[l] and l < r:
                    l += 1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
