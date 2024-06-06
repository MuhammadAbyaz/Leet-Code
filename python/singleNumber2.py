from collections import Counter


def singleNumber(nums: list[int]) -> int:
    numDict = Counter(nums)
    for key in numDict.keys():
        if numDict[key] == 1:
            return key
    return -1


print(singleNumber([2, 2, 3, 2]))
