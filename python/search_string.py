def searchRange(nums, target):
    lo = 0
    hi = len(nums) - 1
    if len(nums) == 1 and nums[0] == target:
        return [0, 0]
    result = [-1, -1]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if lo > hi or hi < lo:
        return [-1, -1]
    if mid == 0 and nums[mid + 1] != target:
        return [mid, mid]
    elif mid == len(nums) - 1 and nums[mid - 1] != target:
        return [mid, mid]
    elif nums[mid + 1] != target and nums[mid - 1] != target:
        return [mid, mid]
    temp_mid = mid
    while temp_mid > 0 and nums[temp_mid] == target:
        temp_mid -= 1
    result[0] = temp_mid + 1 if temp_mid > 0 or nums[temp_mid] != target else 0
    temp_mid = mid
    while temp_mid < len(nums) and nums[temp_mid] == target:
        temp_mid += 1
    result[1] = temp_mid - 1 if temp_mid < len(nums) else len(nums) - 1
    return result


print(searchRange([1, 2, 2], 2))
