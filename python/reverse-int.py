def reverse(x: int) -> int:
    if x < 0:
        num = x * -1
    else:
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
    if x > 0:
        return int(reversed_number) if int(reversed_number).bit_length() < 31 else 0
    return int(reversed_number) * -1 if int(reversed_number).bit_length() < 31 else 0
