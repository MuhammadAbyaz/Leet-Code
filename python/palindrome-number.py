def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    num = x
    length = 0
    temp = num
    while temp != 0:
        length += 1
        temp = temp // 10
    reversed_number = 0
    unit = 10 ** (length - 1)
    while num != 0:
        reversed_number += (num % 10) * unit
        unit = unit / 10
        num = num // 10
    return True if reversed_number == x else False
