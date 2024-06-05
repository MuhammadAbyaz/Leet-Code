def singleNonDuplicate(nums: list[int]) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid % 2 == 1 and nums[mid] != nums[mid - 1]:
            hi = mid
        elif mid % 2 == 0 and nums[mid] != nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return nums[lo]


print(singleNonDuplicate([10, 10, 20, 20, 3, 3, 4, 5, 5]))
