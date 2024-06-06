from collections import Counter


def singleNumber(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    number_dict = Counter(nums)
    return list(filter(lambda key: number_dict[key] == 1, number_dict.keys()))[0]


print(singleNumber([4, 1, 2, 1, 2]))
