def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    numsLength = len(nums)
    l = 0
    res = 0
    hashMap = {}
    for i in range(numsLength):
        hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        while len(hashMap) > k:
            hashMap[nums[l]] -= 1
            if hashMap[nums[l]] == 0:
                del hashMap[nums[l]]
            l += 1
        res += i - l + 1
    return res


print(subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
