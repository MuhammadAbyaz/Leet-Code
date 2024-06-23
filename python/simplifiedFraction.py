from fractions import Fraction


def simplifiedFractions(n: int) -> list[str]:
    if n == 1:
        return []
    res: list[str] = []
    for i in range(2, n + 1):
        for j in range(1, i):
            fraction = str(Fraction(j, i))
            if fraction not in res:
                res.append(fraction)
    return res


print(simplifiedFractions(3))
