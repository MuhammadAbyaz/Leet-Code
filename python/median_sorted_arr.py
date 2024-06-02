def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    mid = float(len(nums1) / 2)
    if len(nums1) % 2 != 0:
        return float(nums1[int(mid - 0.5)])
    else:
        return (nums1[int(mid)] + nums1[int(mid - 1)]) / 2
