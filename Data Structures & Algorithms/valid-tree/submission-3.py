class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        parent = list(range(n))

        def find(u : int) -> int:
            x = parent[u]
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x