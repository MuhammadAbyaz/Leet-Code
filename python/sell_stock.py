def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    minVal = prices[0]
    for val in prices:
        if val < minVal:
            minVal = val
        maxProfit = val - minVal if val - minVal > maxProfit else maxProfit
    return maxProfit


print(maxProfit([2, 1, 4]))
