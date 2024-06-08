def checkSubarraySum(nums: list[int], k: int) -> bool:
    remainderMap = {0: -1}
    sumValue = 0
    for i in range(len(nums)):
        sumValue += nums[i]
        rem = sumValue % k
        if rem in remainderMap:
            if i - remainderMap[rem] > 1:
                return True
        else:
            remainderMap[rem] = i
    return False


print(checkSubarraySum([5, 0, 0, 0], 3))
