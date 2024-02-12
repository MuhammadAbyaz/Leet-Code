# def plusOne(digits):
#     int_str = ""
#     for digit in digits:
#         int_str += str(digit)
#     int_str = str(int(int_str) + 1)
#     return [int(i) for i in int_str]


def plusOne(digits):
    for i in range(1, len(digits) + 1):
        if digits[-i] == 9:
            digits[-i] = 0
        else:
            digits[-i] = digits[-i] + 1
            break
    if digits[0] == 0:
        digits[-i - 1] = 1
    return digits


print(plusOne([1, 2, 3]))
