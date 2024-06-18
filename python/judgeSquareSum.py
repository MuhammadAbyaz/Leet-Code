import math

# def judgeSquareSum(c: int) -> bool:
#     for a in range(int(math.sqrt(c)) + 1):
#         b = math.sqrt(c - a * a)
#         if b == int(b):
#             return True
#     return False


def judgeSquareSum(c: int) -> bool:
    lo = 0
    hi = int(math.sqrt(c))
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if lo * lo + hi * hi == c:
            return True
        if mid * mid + lo * lo == c:
            return True
        elif mid * mid + lo * lo > c:
            hi = mid - 1
        else:
            lo += 1
    return False


print(judgeSquareSum(2 * 31 - 1))
