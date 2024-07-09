def finalPrices(prices: list[int]) -> list[int]:
    stack = []
    n = len(prices)
    for idx, val in enumerate(prices):
        j = idx + 1
        while j < n:
            if prices[j] <= val:
                stack.append(val - prices[j])
                break
            j += 1
        else:
            stack.append(val)
    return stack


print(finalPrices([8, 4, 6, 2, 3]))
