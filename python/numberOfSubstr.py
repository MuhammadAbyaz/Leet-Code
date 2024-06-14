def numberOfSubstrings(s: str) -> int:
    size = len(s)
    hashMap = {"a": 0, "b": 0, "c": 0}
    count = 0
    lo = 0
    for hi in range(size):
        hashMap[s[hi]] = hashMap.get(s[hi], 0) + 1
        while hashMap["a"] and hashMap["b"] and hashMap["c"]:
            count += size - hi
            hashMap[s[lo]] -= 1
            lo += 1
        hi += 1
    return count


print(numberOfSubstrings("abcabc"))
