from math import sqrt


def isThree(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if (n / i) % 1 == 0:
            return True
    return False


print(isThree(12))
