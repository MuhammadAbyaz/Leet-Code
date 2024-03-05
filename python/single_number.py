def singleNumber(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    number_dict = dict()
    for val in nums:
        if number_dict.get(val) is None:
            number_dict[val] = 1
        else:
            number_dict[val] += 1
    for val in nums:
        if number_dict[val] == 1:
            return val


print(singleNumber([2, 2, 1]))
