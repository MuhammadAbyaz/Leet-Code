def majorityElement(nums) -> int:
    number_dict = dict()
    for val in nums:
        if number_dict.get(val) is not None:
            number_dict[val] += 1
        else:
            number_dict[val] = 1
    max_value = [nums[0], number_dict[nums[0]]]
    for key in number_dict:
        if number_dict[key] > max_value[1]:
            max_value[0], max_value[1] = key, number_dict[key]
    return max_value[0]


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
