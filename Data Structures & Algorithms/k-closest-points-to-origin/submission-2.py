class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x, y in points:
            dist = math.pow((0 - x), 2) + math.pow((0 - y), 2)
            dist = math.pow(dist, 0.5)

            heapq.heappush(heap, (dist, x, y))

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res