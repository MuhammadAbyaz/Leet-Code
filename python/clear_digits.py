def clearDigits(s: str) -> str:
    splittedString = list(s)
    for idx, c in enumerate(s):
        if c.isdigit():
            l: int = idx - 1
            splittedString[idx] = "0"
            while l >= 0:
                if not splittedString[l].isdigit():
                    splittedString[l] = "0"
                    break
                l -= 1
    return "".join(filter(lambda x: x != "0", splittedString))


print(clearDigits("cb34"))
