def intersect(nums1, nums2):
    intersection = list()
    for val in nums1:
        if val in nums2:
            intersection.append(val)
            nums2.remove(val)
    return intersection


print(intersect([1, 2, 2, 1], [2, 2]))
