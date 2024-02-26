def removeElement(nums, val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = val
            index += 1
    return index + 1
