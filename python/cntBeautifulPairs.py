from math import gcd
from typing import List


def countBeautifulPairs(nums: List[int]) -> int:
    n = len(nums)
    beautifulPairs = 0
    for idx, num in enumerate(nums):
        val = num % 10
        for j in range(idx):
            n = nums[j]
            while n >= 10:
                n //= 10
            beautifulPairs += gcd(val, n) == 1
    return beautifulPairs


print(countBeautifulPairs([2, 5, 1, 4]))
