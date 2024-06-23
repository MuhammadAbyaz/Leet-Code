def maxSatisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    n = len(customers)
    satisfied = 0
    for i in range(minutes):
        satisfied += customers[i] * grumpy[i]
    maxSatisfied = satisfied

    for i in range(minutes, n):
        satisfied += customers[i] * grumpy[i]
        satisfied -= customers[i - minutes] * grumpy[i - minutes]
        maxSatisfied = max(maxSatisfied, satisfied)
    total = maxSatisfied
    for i in range(n):
        total += customers[i] * (1 - grumpy[i])
    return total


print(maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
