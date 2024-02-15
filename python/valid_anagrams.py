# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for val in s:
        if val in t and s.count(val) == t.count(val):
            result = True
        else:
            result = False
            break
    return result


# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     s_list = [i for i in s]
#     t_list = [i for i in t]
#     s_list.sort()
#     t_list.sort()
#     return s_list == t_list
