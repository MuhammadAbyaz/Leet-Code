def minDays(bloomDay: list[int], m: int, k: int) -> int:
    if (m * k) > len(bloomDay):
        return -1

    def possibleBouquets(bloomDay, k, mid):
        bouquets, adjCount = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                adjCount += 1
            else:
                bouquets += adjCount // k
                adjCount = 0
        bouquets += adjCount / k
        return bouquets

    l = 1
    h = max(bloomDay)
    ans = h
    while l <= h:
        mid = l + (h - l) // 2
        bouquets = possibleBouquets(bloomDay, k, mid)
        if bouquets >= m:
            ans = min(ans, mid)
            h = mid - 1
        else:
            l = mid + 1
    return ans


print(minDays([1, 10, 3, 10, 2], 3, 1))
