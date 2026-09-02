class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # We have a fully connected graph where the weight of each edge is the manhattan distance between the two points.
        # We then use Kahns algorithm to find a minimum spanning tree.
        # This is wrong, Kahns algorithm finds a topological sorting.
        # For a minimal spanning tree we want kruskal or prims algorithm

        n = len(points)
        dsu = DSU(n)

        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort()
        res = 0

        for dist, u, v in edges:
            if dsu.union(u, v): # This returns true if they are not part of the same connected graph yet, they will be when we use this edge.
                res += dist
        return res

