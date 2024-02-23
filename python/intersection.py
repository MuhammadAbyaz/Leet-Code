# def intersection(nums1, nums2):
#     intersection_set = set()
#     for val in nums1:
#         if val in nums2:
#             intersection_set.add(val)
#     return list(intersection_set)


def intersection(nums1, nums2):
    first = set(nums1)
    second = set(nums2)
    return list(first.intersection(second))


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
