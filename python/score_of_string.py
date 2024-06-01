def scoreOfString(s: str) -> int:
    sum = 0
    p1 = 0
    p2 = 1
    while p2 < len(s):
        sum += abs(ord(s[p1]) - ord(s[p2]))
        p1 += 1
        p2 += 1
    return sum


print(scoreOfString("hello"))
