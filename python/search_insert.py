def searchInsert(self, nums: list[int], target: int) -> int:
    i = 0
    j = len(nums) - 1
    while i < j:
        mid = (i + j) // 2
        if target > nums[mid]:
            i = mid + 1
        else:
            j = mid
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return mid + 1
    return mid
