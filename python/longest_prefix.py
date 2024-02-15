def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    for i in range(len(strs[0])):
        prefix += strs[0][i]
        for val in strs:
            if not val.startswith(prefix):
                prefix = prefix[0 : len(prefix) - 1]
                return prefix
    return prefix
