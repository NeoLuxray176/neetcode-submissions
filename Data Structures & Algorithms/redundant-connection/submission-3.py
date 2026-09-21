class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Try to build an MST and on the first redundant connection, we have found our solution
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

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