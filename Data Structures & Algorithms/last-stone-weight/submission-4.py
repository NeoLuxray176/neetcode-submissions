class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            a, b = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if a == b:
                continue
            else:
                heapq.heappush_max(stones, a - b)

        return stones[0]