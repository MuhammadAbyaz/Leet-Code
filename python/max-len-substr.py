def maximumLengthSubstring(s: str):
    if s == "":
        return 0
    elif len(s) == 1:
        return 1
    lenSubstr = 0
    strSet = set(s)
    for i in range(len(s)):
        substring = ""
        for j in range(i, len(s)):
            if substring.count(s[j]) < 2:
                substring += s[j]
            else:
                break
        for val in substring:
            if val not in strSet:
                break
        else:
            if lenSubstr < len(substring):
                lenSubstr = len(substring)
    return lenSubstr
