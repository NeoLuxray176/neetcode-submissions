class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        # min-heap and always pick the next smallest node, then iterate over all
        # edges and update the distances

        dists = [float("inf")] * (n + 1)

        adj_list = [[] for _ in range(n + 1)]

        for u, v, t in times:
            adj_list[u].append([v, t])

        heap = [[0, k]]
        dists[k] = 0

        while heap:
            dist, u = heapq.heappop(heap)

            if dist > dists[u]:
                continue

            for v, t in adj_list[u]:
                if dists[v] > dists[u] + t:
                    dists[v] = dists[u] + t
                    heapq.heappush(heap, [dists[v], v])

        # print(dists)
        if max(dists[1:]) == float("inf"):
            return -1
        return max(dists[1:])



