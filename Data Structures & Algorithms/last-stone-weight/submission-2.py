class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            a, b = heapq.heappop_max(heap), heapq.heappop_max(heap)

            if a == b:
                continue
            else:
                c = a - b
                heapq.heappush_max(heap, c)

        if len(heap) == 1:
            return heap[0]
        
        return 0