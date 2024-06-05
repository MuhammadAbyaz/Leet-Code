def longestPalindrome(s: str) -> int:
    hashMap: dict[str, int] = dict()
    for c in s:
        hashMap[c] = hashMap.get(c, 0) + 1
    length = 0
    oddFrequency = False
    for val in hashMap.values():
        if val % 2 == 0:
            length += val
        else:
            length += val - 1
            oddFrequency = True
    if oddFrequency:
        return length + 1
    return length


print(longestPalindrome("bananas"))
