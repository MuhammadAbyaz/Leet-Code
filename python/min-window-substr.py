def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    t_dict: dict[str, int] = dict()
    window: dict[str, int] = dict()
    for char in t:
        t_dict[char] = 1 + t_dict.get(char, 0)
    have, need = 0, len(t_dict)
    l = 0
    res, res_len = [-1, -1], float("infinity")
    for r in range(len(s)):
        window[s[r]] = 1 + window.get(s[r], 0)
        if s[r] in t_dict and window[s[r]] == t_dict[s[r]]:
            have += 1
        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            window[s[l]] -= 1
            if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1] if res_len != float("infinity") else ""


print(minWindow("ADOBECODEBANC", "ABC"))
