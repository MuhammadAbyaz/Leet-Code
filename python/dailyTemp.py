from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = []
    n = len(temperatures)
    for i in range(1, n):
        if temperatures[i] > temperatures[i - 1]:
            res.append(1)
            continue
        j = i + 1
        cnt = 2
        while j < n and temperatures[j] < temperatures[i - 1]:
            cnt += 1
            j += 1
        (
            res.append(cnt)
            if j < n and temperatures[j] > temperatures[i - 1]
            else res.append(0)
        )
    res.append(0)
    return res


print(dailyTemperatures([30, 40, 50, 60]))
