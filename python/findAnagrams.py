def findAnagrams(s: str, p: str) -> list[int]:
    lo = 0
    hi = len(p)
    sLen = len(s)
    sortedP = list(p)
    sortedP.sort()
    res = []
    while hi <= sLen:
        window = list(s[lo:hi])
        window.sort()
        if window == sortedP:
            res.append(lo)
        hi += 1
        lo += 1
    return res


print(findAnagrams("abab", "ab"))
