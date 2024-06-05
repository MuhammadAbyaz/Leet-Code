def appendCharacters(s: str, t: str) -> int:
    p1 = 0
    p2 = 0
    s_len = len(s)
    t_len = len(t)
    while p1 < s_len and p2 < t_len:
        if s[p1] == t[p2]:
            p2 += 1
        p1 += 1
    return t_len - p2


print(appendCharacters("vrykt", "rkge"))
