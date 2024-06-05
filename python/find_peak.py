def findPeakElement(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
