class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # General Idea of Bellman-Ford
        # Keep array of distances initially set to infinity except for the source
        # Iterate over all edges n - 1 times and update paths if there is now a shorter paht

        dists = [float("inf")] * (n + 1)
        dists[k] = 0

        for _ in range(n - 1):
            changed = False
            for u, v, weight in times:
                if dists[u] + weight < dists[v]:
                    dists[v] = dists[u] + weight
                    changed = True
            if not changed:
                break

        res = 0
        for i, dist in enumerate(dists):
            if i < 1:
                continue
            if dist == float("inf"):
                return -1
            res = max(res, dist)
        
        return res