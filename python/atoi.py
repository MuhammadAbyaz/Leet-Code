def myAtoi(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    num = []
    i = 0
    while i < len(s) and ((i == 0) and s[i] in ["-", "+"] or s[i].isdigit()):
        num.append(s[i])
        i += 1
    try:
        result = int("".join(num))
    except:
        return 0
    if result < -(2**31):
        return -(2**31)
    elif result > 2**31 - 1:
        return 2**31 - 1
    else:
        return result


print(myAtoi("-13+2"))
