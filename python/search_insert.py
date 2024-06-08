def searchInsert(nums: list[int], target: int) -> int:
    if target > nums[len(nums) - 1]:
        return len(nums)
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return mid + 1
    return mid


print(searchInsert([1, 3, 5, 6], 2))
