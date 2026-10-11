class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for u, v in edges:
            n = max(n, u, v)

        parent = list(range(n + 1))
        size = [1] * (n + 1)


        def find(x : int) -> int:
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
