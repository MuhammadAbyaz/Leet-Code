def rotate(self, nums, k: int) -> None:
    loop_range = 0
    length = len(nums)
    if k % length == 0:
        return nums
    else:
        for i in range(k, 0, -1):
            if i % length == 0:
                break
            else:
                loop_range += 1
    for i in range(loop_range):
        last_element = nums.pop()
        nums.insert(0, last_element)
