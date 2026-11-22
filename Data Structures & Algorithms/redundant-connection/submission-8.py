class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            u, v = find(a), find(b)

            if u == v:
                return [a, b]

            if size[u] < size[v]:
                u, v = v, u

            parent[v] = u
            size[u] += size[v]

        return [-1, -1]