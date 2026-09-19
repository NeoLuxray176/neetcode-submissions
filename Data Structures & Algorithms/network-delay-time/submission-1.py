class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # General Idea
        # Bellman Ford
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        for _ in range(n):
            changed = False
            for u, v, time in times:
                # print(dist[u], time, dist[v])
                if dist[u] + time > dist[v]:
                    continue
                else:
                    dist[v] = dist[u] + time
                    changed = True

            if not changed:
                break

        if max(dist[1:]) == float("inf"):
            return -1
        else:
            return max(dist[1:])