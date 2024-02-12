def merge(nums1: list, m, nums2, n):
    result = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    while i < m:
        result.append(nums1[i])
        i += 1
    while j < n:
        result.append(nums2[j])
        j += 1
    nums1.clear()
    nums1.extend(result)
