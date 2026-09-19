class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # General Idea of Dijkstra
        # Given an adjacency list
        # Keep an array of distances
        # Then have a minheap with the next paths we can explore

        graph = [[] for _ in range(n + 1)]
        for u, v, weight in times:
            graph[u].append((weight, v))

        dists = [float("inf")] * (n + 1)
        dists[k] = 0
        heap = [(k, 0)]

        while heap:
            u, distance = heapq.heappop(heap)

            if distance != dists[u]:
                continue

            for weight, v in graph[u]:
                candidate = distance + weight
                if candidate < dists[v]:
                    dists[v] = candidate
                    heapq.heappush(heap, (v, candidate))

        if max(dists[1:]) == float("inf"):
            return -1

        return max(dists[1:])


