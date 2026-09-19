class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra uses an adjacency list
        # We have an array that stores the distances
        # We then start with the source and add it to a min heap sorted by the edge weight
        # we iterate over all edges going out from the top node and update the corresponding distances
        # if they are lower, if we update a distance we add the corresponding node and its weight to the heap

        graph = [[] for _ in range(n + 1)]

        for u, v, weight in times:
            graph[u].append((v, weight))

        dists = [float("inf")] * (n + 1)
        dists[k] = 0
        heap = [(k, 0)] # node, weight

        while heap:
            u, weight = heapq.heappop(heap)

            if weight != dists[u]:
                continue

            for v, dist in graph[u]:
                candidate = weight + dist
                if candidate < dists[v]:
                    dists[v] = candidate
                    heapq.heappush(heap, (v, candidate))

        if max(dists[1:]) == float("inf"):
            return -1
        
        return max(dists[1:])
