def commonChars(words: list[str]) -> list[str]:
    frq: dict[str, int] = dict()
    for val in words[0]:
        frq[val] = frq.get(val, 0) + 1
    for i in range(1, len(words)):
        wordfrq: dict[str, int] = dict()
        for val in words[i]:
            wordfrq[val] = wordfrq.get(val, 0) + 1
        for val in frq.keys():
            if wordfrq.get(val) != None:
                frq[val] = min(frq[val], wordfrq[val])
            else:
                frq[val] = 0
    res = []
    for key in frq.keys():
        if frq[key] > 0:
            for _ in range(frq[key]):
                res.append(key)
    return res


print(commonChars(["bella", "label", "roller"]))
