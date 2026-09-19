class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims Algorithm
        # Works by computing all weights, adding them to an array
        # and then processing the sorted array.
        # We keep track of nodes we have already added to the MST
        # using a visited array

        n = len(points)
        res = 0
        visited = [False] * (n)

        heap = [(0, 0)]

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