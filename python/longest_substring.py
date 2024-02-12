def lengthOfLongestSubstring(s):
    length = 0

    for i in range(len(s)):
        result = ""
        for j in range(i, len(s)):
            if s[j] not in result:
                result += s[j]
            else:
                break
        if len(result) > length:
            length = len(result)
    return length


print(lengthOfLongestSubstring("abcabcbb"))
