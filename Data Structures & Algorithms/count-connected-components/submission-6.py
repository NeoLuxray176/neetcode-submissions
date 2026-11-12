class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        count = [1] * n

        def find(x : int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            a, b = find(u), find(v)

            if a == b:
                continue

            if count[a] < count[b]:
                a, b = b, a

            parent[b] = a
            count[a] += count[b]

        for i in range(n):
            find(i)

        return len(set(parent))