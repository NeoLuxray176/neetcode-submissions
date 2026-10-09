class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            a, b = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if a != b:
                heapq.heappush_max(stones, a - b)

        if not stones:
            return 0
        return stones[0]