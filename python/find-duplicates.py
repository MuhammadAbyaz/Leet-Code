def findDuplicates(nums: list[int]) -> list[int]:
    result: list[int] = []
    n: int = len(nums)
    for i in range(n):
        num = abs(nums[i])
        idx: int = num - 1
        if nums[idx] < 0:
            result.append(num)
        nums[idx] *= -1
    return result


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
