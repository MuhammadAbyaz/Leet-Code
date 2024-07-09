def findTheWinner(n: int, k: int) -> int:
    circularGame: list[int] = list(range(1, n + 1))
    lastIndex = 0
    while n > 1:
        lastIndex += k - 1
        if lastIndex >= n:
            lastIndex %= n
            circularGame.pop(lastIndex)
        else:
            circularGame.pop(lastIndex)
        n -= 1

    return circularGame[0]


print(findTheWinner(10, 2))
