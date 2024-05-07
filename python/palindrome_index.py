def main():
    s = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
    flag = 0
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            flag = 1
            break
    if flag:
        if s[l] == s[r - 1] and s[l + 1] == s[r - 2]:
            return r
        else:
            return l
    else:
        return -1


print(main())
