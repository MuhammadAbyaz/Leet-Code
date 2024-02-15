def containsDuplicate(self, nums) -> bool:
    nums_set = set(nums)
    if len(nums_set) == len(nums):
        return False
    return True
