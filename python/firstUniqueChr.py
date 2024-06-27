from collections import Counter


def firstUniqChar(s: str) -> int:
    freq = Counter(list(s))
    for idx, val in enumerate(s):
        if freq[val] == 1:
            return idx
    return -1


print(firstUniqChar("loveleetcode"))
