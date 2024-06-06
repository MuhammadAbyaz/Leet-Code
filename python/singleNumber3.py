from collections import Counter


def singleNumber(nums: list[int]) -> list[int]:
    numDict = Counter(nums)
    res: list[int] = []
    for key in numDict.keys():
        if numDict[key] == 1:
            res.append(key)
    return res
