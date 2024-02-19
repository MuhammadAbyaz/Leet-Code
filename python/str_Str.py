def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    else:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                index = i
                value = ""
                for j in range(0, len(needle)):
                    if haystack[i + j] == needle[j]:
                        value += haystack[i + j]
                    else:
                        break
                if value == needle:
                    return index


print(strStr("sadbutsad", "sad"))
