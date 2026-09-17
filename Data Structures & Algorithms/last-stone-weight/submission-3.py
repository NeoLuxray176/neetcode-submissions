class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while heap and len(heap) > 1:
            a, b = heapq.heappop_max(heap), heapq.heappop_max(heap)

            if a == b:
                continue
            else:
                heapq.heappush_max(heap, a - b)

        if not heap:
            return 0
        
        return heap[-1]