def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    if abs(divisor) == 1:
        return dividend * divisor
    if dividend < divisor:
        return 0
    if dividend == divisor:
        return 1
    isNegative = False
    quotient = 0
    if (divisor < 0 or dividend < 0) and not ((dividend < 0 and divisor < 0)):
        isNegative = True
    divisor = abs(divisor)
    dividend = abs(dividend)
    while dividend >= divisor:
        x = 1
        b = divisor
        while b <= (dividend >> 1):
            b = b << 1
            x = x << 1
        quotient += x
        dividend -= b
    if isNegative:
        return quotient * -1
    return quotient


print(divide(9, 3))
