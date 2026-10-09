class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = ((x - 0) + (y - 0)) ** 2

            heapq.heappush_max(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _, x, y in heap:
            res.append([x,y])
        return res