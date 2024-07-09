def backspaceCompare(s: str, t: str) -> bool:
    s1: list[str] = []
    s2: list[str] = []
    for val in s:
        if s1 and val == "#":
            s1.pop()
        elif val != "#":
            s1.append(val)
    for val in t:
        if s2 and val == "#":
            s2.pop()
        elif val != "#":
            s2.append(val)
    return "".join(s1) == "".join(s2)


print(backspaceCompare("y#fo##f", "y#f#o##f"))
