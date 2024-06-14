def heightChecker(heights: list[int]) -> int:
    expected = heights.copy()
    expected.sort()
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            cnt += 1
    return cnt
