def kthFactor(n: int, k: int) -> int:
    cnt = 1
    for i in range(2, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return i
    return -1


print(kthFactor(4, 4))
