import math


def commonFactors(a: int, b: int) -> int:
    if a == 1 or b == 1:
        return 1
    greatestCommonDivisor = math.gcd(a, b)
    cnt = 1
    for i in range(2, greatestCommonDivisor + 1):
        if a % i == 0 and b % i == 0:
            cnt += 1
    return cnt


print(commonFactors(12, 6))
