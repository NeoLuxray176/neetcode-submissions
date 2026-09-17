class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # This is prims algorithm with the solution from https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/6280134/video-improved-prims-algorithm-solution-vh1as
        n = len(points)

        min_cost = 0
        visited = [False] * n
        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)

            if visited[u]:
                continue
            
            visited[u] = True
            min_cost += cost

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(pq, (dist, v))

        return min_cost