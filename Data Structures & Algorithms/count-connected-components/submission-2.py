class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)

            for neighbor in adj_list[i]:
                dfs(neighbor)
            return

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res
