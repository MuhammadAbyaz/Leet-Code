# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    count = 0
    is_consistent: bool = True
    for word in words:
        for char in word:
            if char not in allowed:
                is_consistent = False
                break
            else:
                is_consistent = True
        if is_consistent:
            count += 1

    return count
