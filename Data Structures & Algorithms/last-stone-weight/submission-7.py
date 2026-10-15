class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush_max(heap, stone)

        while len(heap) > 1:
            x, y = heapq.heappop_max(heap), heapq.heappop_max(heap)

            if x == y:
                continue
            else:
                # x > y
                heapq.heappush_max(heap, x - y)

        if heap:
            return heap[0]
        else:
            return 0