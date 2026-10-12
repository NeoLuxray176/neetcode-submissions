class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float("inf")] * n
        dists[src] = 0

        adj_list = [[] for _ in range(n)]

        for u, v, price in flights:
            adj_list[u].append([price, v])

        for _ in range(k + 1):
            changed = False
            new_dists = dists.copy()
            for u in range(n):
                for price, v in adj_list[u]:
                    if dists[v] > dists[u] + price:
                        new_dists[v] = min(new_dists[v], dists[u] + price) 
                        changed = True
            dists = new_dists
            if not changed:
                break

        if dists[dst] == float("inf"):
            return -1
        return dists[dst]

