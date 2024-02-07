def isValid(s):
    opening = ["{", "[", "("]
    closing = ["}", "]", ")"]
    resultant_list = []
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return False
    for val in s:
        if val in opening:
            resultant_list.append(val)
        else:
            if len(resultant_list) == 0 or closing.index(val) != opening.index(
                resultant_list[len(resultant_list) - 1]
            ):
                return False
            else:
                resultant_list.pop()
    if len(resultant_list) == 0:
        return True
    return False


print(isValid(")("))
