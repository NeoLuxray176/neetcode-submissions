class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        adj_list = [[] for _ in range(n)]

        for i, (x, y) in enumerate(points):
            for j, (u, v) in enumerate(points):
                if i == j:
                    continue
                dist = abs(x - u) + abs(y - v)
                adj_list[i].append([dist, j])

        heap = [[-1, 0, 0]]
        tree = []
        visited = set()

        while heap:
            d, u, v = heapq.heappop(heap)

            if v in visited:
                continue
            visited.add(v)

            if d != -1:
                tree.append(d)

            for d, w in adj_list[v]:
                if w not in visited:
                    heapq.heappush(heap, [d, v, w])

        print(tree)
        return sum(tree)