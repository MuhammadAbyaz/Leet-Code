def twoSum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            break
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
            while numbers[l - 1] == numbers[l] and l < r:
                l += 1
    return [l + 1, r + 1]


print(twoSum([2, 2, 5, 5, 7], 12))
