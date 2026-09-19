class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman-Ford
        # General Idea
        # We set up an array tracking the distances with initial value infinity
        # We set the source's distance to zero.
        # Then we iterate over all edges V - 1 times and try to find new shortest pahts
        # from now potentially reachable nodes. Note that initially only the source is reachable
        # In the end we will have an array of shortest distances.

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

        if max(dists[1:]) == float("inf"):
            return -1

        return max(dists[1:])