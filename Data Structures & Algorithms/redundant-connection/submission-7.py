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

        for u, v in edges:
            a, b = find(u), find(v)

            if a == b:
                return [u, v]

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        return [-1, -1]