def maxProfitAssignment(
    difficulty: list[int], profit: list[int], worker: list[int]
) -> int:
    maxProfit = 0
    diff_prof = [val for val in zip(difficulty, profit)]
    diff_prof.sort()
    worker.sort()
    n = len(worker)
    diff_len = len(difficulty)
    for i in range(n):
        ptr = 0
        bestProfit = 0
        while ptr < diff_len and worker[i] >= diff_prof[ptr][0]:
            bestProfit = max(bestProfit, diff_prof[ptr][1])
            ptr += 1
        maxProfit += bestProfit
    return maxProfit


print(maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
