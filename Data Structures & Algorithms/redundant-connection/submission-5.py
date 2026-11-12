class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-find
        n = len(edges) + 1

        parent = list(range(n))
        count = [1] * n

        def find(x : int):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            a, b = find(u), find(v)

            if a == b:
                return [u, v]

            if count[a] < count[b]:
                a, b = b, a

            parent[b] = a
            count[a] += count[b]

        return [-1, -1]

