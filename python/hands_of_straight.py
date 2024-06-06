from collections import Counter


def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    length = len(hand)
    if length % groupSize != 0:
        return False
    freq = dict(sorted(Counter(hand).items()))
    while freq:
        arr = []
        start = next(iter(freq))
        for i in range(groupSize):
            current = start + i
            if current not in freq:
                return False
            if not arr or arr[len(arr) - 1] + 1 == current:
                arr.append(current)
                if freq[current] - 1 == 0:
                    del freq[current]
                else:
                    freq[current] -= 1
                current += 1
    return True


print(isNStraightHand([1, 2, 3, 4, 5], 4))
