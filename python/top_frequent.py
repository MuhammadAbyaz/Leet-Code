def topKFrequent(nums, k):
    hashMap = {}
    result = []
    for val in nums:
        hashMap[val] = 1 + hashMap.get(val, 0)
    for _ in range(k):
        maxValue = max(hashMap.values())
        for val in hashMap.keys():
            if hashMap[val] == maxValue:
                hashMap.pop(val)
                result.append(val)
                break
    return result

