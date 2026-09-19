class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Using Kruskals MST Algorithm
        # Kruskal uses union-find to find the next unconnected component
        # It adds the smaller subtree to the larger subtree
        n = len(points)
        size = [1] * n
        parent = list(range(n)) # every node is its own parent

        def find(x : int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]] # compact

                x = parent[x]

            return x

        edges = []
        tree = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                new_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                edges.append((new_dist, i, j))

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
        for dist, a, b in tree:
            res += dist

        return res