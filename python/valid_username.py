def possibleChanges(usernames):
    results = []
    for username in usernames:
        result = False
        for i in range(len(username)):
            if result:
                break
            for j in range(i, len(username)):
                if username[j] < username[i]:
                    results.append("YES")
                    result = True
                    break
        if not result:
            results.append("NO")
    return results


print(possibleChanges(["baz"]))
