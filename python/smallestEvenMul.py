import math


def smallestEvenMultiple(n: int) -> int:
    return n // math.gcd(n, 2) * 2
