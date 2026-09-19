class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims Algorithm
        # Works by computing all weights, adding them to an array
        # and then processing the sorted array.
        # We keep track of nodes we have already added to the MST
        # using a visited array

        n = len(points)
        size = [1] * n
        parent = list(range(n))

        def find(x : int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        edges = []
        tree = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        for dist, u, v in sorted(edges):
            a, b = find(u), find(v)

            if a == b:
                continue

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]
            tree.append((dist, a, b))

        if len(tree) != n - 1:
            return -1

        res = 0

        for dist, _, _ in tree:
            res += dist

        return res