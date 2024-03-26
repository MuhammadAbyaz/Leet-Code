def findDuplicate(nums: list[int]) -> int:
    hare = nums[0]
    tortoise = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
