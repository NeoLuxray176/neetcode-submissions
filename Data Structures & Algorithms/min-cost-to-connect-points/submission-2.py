class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        res = 0
        visited = [False] * n
        
        queue = [(0, 0)] # distance, index of point in list

        while queue:
            dist, v = heapq.heappop(queue)

            if visited[v]:
                continue


            visited[v] = True
            res += dist

            for u in range(len(points)):
                if visited[u]:
                    continue
                new_dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                
                heapq.heappush(queue, (new_dist, u))

        return res