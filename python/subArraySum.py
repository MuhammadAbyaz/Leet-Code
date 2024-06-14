def subarraysDivByK(nums: list[int], k: int) -> int:
    remainder = {0: 1}
    subArrayCount = 0
    sum = 0
    for val in nums:
        sum += val
        rem = sum % k
        if rem < 0:
            rem += k
        if remainder.get(rem) != None:
            subArrayCount += remainder[rem]
            remainder[rem] += 1
        else:
            remainder[rem] = 1
    return subArrayCount


print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
