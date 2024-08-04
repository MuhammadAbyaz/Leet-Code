from typing import List
def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    new_arr = []
    for i in range(n):
        new_arr.append(nums[i])
        total = nums[i]
        for j in range(i+1,n):
            total+= nums[j]
            new_arr.append(total)
    new_arr.sort()
    return sum(new_arr[left-1:right])

print(rangeSum([1,2,3,4],4,3,4))
