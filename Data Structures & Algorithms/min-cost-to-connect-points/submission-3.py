class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algorithm
        # Uses a visited array to skip nodes that are already connected
        # Then iterates over the points with a min-heap

        n = len(points)
        visited = [False] * n
        res = 0

        heap = [(0, 0)] # distance and point index

        while heap:
            dist, u = heapq.heappop(heap)

            if visited[u]:
                continue

            visited[u] = True
            res += dist

            for v in range(n):
                if visited[v]:
                    continue
                new_dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])

                heapq.heappush(heap, (new_dist, v))

        return res