# def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
#     res = []
#     length = len(arr1)
#     for val in arr2:
#         s = 0
#         while s < length:
#             if arr1[s] == val:
#                 res.append(arr1[s])
#                 arr1[s] = -1
#             s += 1
#     res.extend(list(filter(lambda x: x > 0, arr1)))
#     return res

from collections import Counter


def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    hashMap = dict(sorted(Counter(arr1).items()))
    res = []
    for val in arr2:
        res.extend([val] * hashMap[val])
        hashMap[val] = 0
    for key in hashMap:
        if hashMap[key] > 0:
            res.extend([key] * hashMap[key])
    return res


print(relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
