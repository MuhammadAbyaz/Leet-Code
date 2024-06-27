def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    queue = [[idx, val] for idx, val in enumerate(tickets)]
    sec = 0
    while queue:
        val = queue.pop(0)
        val[1] -= 1
        if val[0] == k and val[1] == 0:
            return sec + 1
        if val[1] != 0:
            queue.append(val)
        sec += 1
    return sec


print(timeRequiredToBuy([2, 3, 2], 2))
