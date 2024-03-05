def isPerfectSquare(num: int) -> bool:
    return (num ** (1 / 2)) % 1 == 0


print(isPerfectSquare(16))
