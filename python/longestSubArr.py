import heapq


def longestSubarray(nums: list[int], limit: int) -> int:
    l, r, n = 0, 0, len(nums)
    maxHeap: list = []
    minHeap: list = []
    maxLen = 0
    while r < n:
        heapq.heappush(maxHeap, (-nums[r], r))
        heapq.heappush(minHeap, (nums[r], r))
        while -maxHeap[0][0] - minHeap[0][0] > limit:
            l = min(maxHeap[0][1], minHeap[0][1]) + 1
            while maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            while minHeap[0][1] < l:
                heapq.heappop(minHeap)
        maxLen = max(maxLen, r - l + 1)
        r += 1
    return maxLen


print(longestSubarray([8, 2, 4, 7], 4))
