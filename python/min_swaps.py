from typing import List
def minSwaps(nums: List[int]) -> int:
    n = len(nums)
    oneCount = nums.count(1)
    if oneCount == 0 or oneCount == n:
        return 0
    win = sum(nums[:oneCount])
    maxi = win
    for i in range(n):
        win -= nums[i]
        win += nums[(i+oneCount) % n]
        maxi = max(maxi, win)
    return oneCount - maxi
print(minSwaps([1,1,0,0,1]))
