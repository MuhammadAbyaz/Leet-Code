# def sortArrayByParity(nums):
#     result = []
#     i = 0
#     while i < len(nums):
#         if nums[i] % 2 == 0:
#             result.append(nums[i])
#         i += 1
#     i = 0
#     while i < len(nums):
#         if nums[i] % 2 != 0:
#             result.append(nums[i])
#         i += 1
#     return result


def sortArrayByParity(nums):
    last_even = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[last_even], nums[i] = nums[i], nums[last_even]
            last_even += 1
    return nums


nums = [3, 1, 2, 4]
sortArrayByParity(nums)
print(nums)
